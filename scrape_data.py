import json
from translate import Translator
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor
import threading

# Load existing data
def load_data(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

datascience = load_data("datascience.json")
robotics = load_data("robotics.json")
multimedia = load_data("multimedia.json")

def save(_file, data):
    with open(_file, "w") as file:
        json.dump(data, file, indent=2)

# Set up Chrome options to run headless (without opening a visible browser window)
chrome_options = Options()
chrome_options.add_argument('--headless')

# Set up a lock for threading
lock = threading.Lock()

# Cache for translations
translation_cache = {}

# Function to translate the name
def translate_name(arabic_name):
    if arabic_name in translation_cache:
        return translation_cache[arabic_name]
    translator = Translator(to_lang="en", from_lang="ar")
    translation = translator.translate(arabic_name)
    translation_cache[arabic_name] = translation
    return translation

def get_data_for_seat(seat_no, letter, department, file):
    with webdriver.Chrome(options=chrome_options) as driver:
        url = f'http://app1.helwan.edu.eg/Computer{letter}/HasasnUpMlist.asp?z_sec=LIKE&z_gro=%3D&z_dep=%3D&z_st_name=LIKE&z_st_settingno=%3D&x_st_settingno={seat_no}&x_st_name=&psearch=&Submit=++++%C8%CD%CB++++'

        # Load the webpage
        driver.get(url)

        # Get the page source
        html_source = driver.page_source

        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(html_source, 'html.parser')
        a_tags = soup.find_all('a')
        a_on_line_294 = a_tags[-1]
        href_value = a_on_line_294.get('href')
        std_code = href_value.split('=')[-1]

        if std_code == "reset":  # this will happen if the seat number is not found
            print(f"Couldn't store the data for the seat number: '{seat_no}' (seat number not found)")
            return

        url = f"http://app1.helwan.edu.eg/Computer{letter}/HasasnUpMview.asp?StdCode={std_code}"
        driver.get(url)
        html_source = driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')

        # store name (translated in english) and full mark
        arabic_name = driver.find_element(By.XPATH, "/html/body/form/div/table[1]/tbody/tr[3]/td[2]/div/font/b").text
        name = translate_name(arabic_name)
        full_mark = int(driver.find_element(By.XPATH, "/html/body/form/div/table[4]/tbody/tr[3]/td[1]/div/font/b").text)

        # get marks
        td_elements = soup.find_all('td', {'width': '100'})  # Find all <td> elements with width="100"
        int_values = [int(td.text.strip()) for td in td_elements if td.text.strip().isdigit()]

        langs = ["English", "Social Issues", "IS", "Discrete Math", "CS", "Mathematics"]
        marks_dict = {langs[i]: int_values[i] for i in range(min(len(langs), len(int_values)))}

        # store gpa
        gpa_element = driver.find_element(By.XPATH, "/html/body/form/div/table[4]/tbody/tr[3]/td[6]/div/font/b")
        gpa = float(gpa_element.text) if gpa_element.text else 0.0

        # get rating
        gpa_ranges = {1: "Very Weak", 2: "Weak", 2.5: "Acceptable", 3: "Good", 3.5: "Very Good"}
        rating = next((value for threshold, value in gpa_ranges.items() if gpa < threshold), "Excellent")

        # store the data
        data = {
            "Seat Number": seat_no,
            "Name": name,
            "Marks": marks_dict,
            "Full Mark": full_mark,
            "GPA": gpa,
            "Rating": rating
        }

        with lock:
            department.append(data)
            save(file, department)
            print(f"Stored the data for the seat number: '{seat_no}' successfully")

def get_data(start_seat_no, end_seat_no, letter, department, file):
    with ThreadPoolExecutor(max_workers=5) as executor:
        for seat_no in range(start_seat_no, end_seat_no + 1):
            executor.submit(get_data_for_seat, seat_no, letter, department, file)

