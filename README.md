# Scrape&Analyze students data
this project scrapes the students marks from the faculty's website and analyze it

# Prerequisites
Before running the main.py file, ensure you have the following libraries installed. You can install them using pip, which is the package installer for Python. Follow the steps below to install the required libraries.

## Installation
    Ensure you have Python installed:
        Download and install Python from the official website: Python.org.

    pip is usually included with Python. You can check if pip is installed by running the following command in your terminal or command prompt: pip --version

If pip is not installed, you can download it by following the instructions here.

Install required libraries:

    Open your terminal or command prompt and navigate to the project directory where main.py is located.

    Run the following command to install all required libraries:

    pip install json5 translate BeautifulSoup4 selenium pandas

    Additional Setup for Selenium:
        Selenium requires a WebDriver to interface with the browser. For Chrome, you need to download the ChromeDriver that matches your Chrome browser version from here.
        Once downloaded, place the chromedriver executable in a directory included in your system's PATH, or specify the path to chromedriver in your code.

Installing Specific Libraries:

    If you prefer to install each library individually, you can use the following commands:
        pip install json5
        pip install translate
        pip install beautifulsoup4
        pip install selenium
        pip install pandas

Example

Here is an example of how to run the main.py file once all the libraries are installed:

    Open your terminal or command prompt.
    Navigate to the project directory:

    bash

cd /path/to/your/project

Run the main.py file:

bash

    python main.py

Main Libraries Used
json5

    This library is used for reading and writing JSON files with a relaxed JSON format, which is easier to read and write.

translate

    This library provides translation services.

re

    This is the regular expression library used for string matching and manipulation.

bs4 (BeautifulSoup)

    This library is used for parsing HTML and XML documents. It is commonly used for web scraping.

selenium

    This library is used for automating web browser interaction. It requires a WebDriver to interface with the chosen web browser.

pandas

    This library is used for data manipulation and analysis. It provides data structures and functions needed to manipulate numerical tables and time series.
