# Scrape & Analyze Students Data

This project scrapes student marks from the faculty's website and performs analysis on the data.

## Prerequisites

Before running the `main.py` file, ensure you have the following libraries installed. You can install them using `pip`, the Python package installer. Follow the steps below to install the required libraries.

## Installation

### 1. Ensure Python is Installed
Download and install Python from the official website: [Python.org](https://www.python.org/downloads/).

You can check if Python is installed by running the following command in your terminal or command prompt:
```bash
python --version
```

### 2. Ensure `pip` is Installed
`pip` is usually included with Python. To check if it’s installed, run:
```bash
pip --version
```

If `pip` is not installed, you can follow the installation guide here: [Installing pip](https://pip.pypa.io/en/stable/installation/).

### 3. Install Required Libraries
Open your terminal or command prompt and navigate to the directory where `main.py` is located. Then, run the following command to install all required libraries:
```bash
pip install json5 translate beautifulsoup4 selenium pandas
```

#### Additional Setup for Selenium:
Selenium requires a WebDriver to interact with the browser. For Chrome, follow these steps:
1. Download the ChromeDriver that matches your Chrome browser version from [here](https://sites.google.com/chromium.org/driver/).
2. Place the `chromedriver` executable in a directory included in your system’s PATH, or specify the path to the `chromedriver` in your code.

### 4. Installing Libraries Individually

If you prefer to install each library individually, you can run the following commands:
```bash
pip install json5
pip install translate
pip install beautifulsoup4
pip install selenium
pip install pandas
```

## Example: Running the `main.py` File

Once all the libraries are installed, follow these steps to run the `main.py` file:

1. Open your terminal or command prompt.
2. Navigate to the project directory:
    ```bash
    cd /path/to/your/project
    ```
3. Run the `main.py` file:
    ```bash
    python main.py
    ```

## Main Libraries Used

### 1. **json5**
- This library is used for reading and writing JSON files with a relaxed format, making it easier to read and write JSON data.

### 2. **translate**
- Provides translation services to translate text from one language to another.

### 3. **re (Regular Expressions)**
- A library for pattern matching and manipulation of strings.

### 4. **bs4 (BeautifulSoup)**
- A popular library for parsing HTML and XML documents, commonly used for web scraping tasks.

### 5. **selenium**
- A powerful library for automating browser interaction. It requires a WebDriver to interface with the chosen web browser.

### 6. **pandas**
- A library for data manipulation and analysis, providing powerful data structures for handling numerical tables and time series data.
