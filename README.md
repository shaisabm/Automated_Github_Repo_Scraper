# GitHub Repository Scraper

This Python script is designed to scrape GitHub repositories based on a given search keyword and then gather all the files from the individual repositories. It utilizes web scraping techniques using BeautifulSoup for parsing HTML content and Selenium for navigating through web pages dynamically.

## Features

### Repository Scraping
- Scrapes repositories from GitHub based on a specified search keyword.
- Filters out repositories based on certain criteria.
- Writes the repository URLs into a file named `repo.txt`.

### File Gathering
- Navigates through each repository listed in `repo.txt`.
- Extracts all files present in the repositories and writes their URLs into a file named `all_files.txt`.

## Instructions

1. **Search Keyword Input**: When prompted, enter the search keyword. You can use '+' to represent spaces in multi-word searches.

2. **Scraping Repositories**: The script will scrape GitHub for repositories matching the search keyword. It will continue scraping across multiple pages until all repositories are gathered. The URLs of these repositories will be saved in `repo.txt`.

3. **Gathering Files**: The script will then navigate through each repository listed in `repo.txt`, extracting all files present in the repositories. The URLs of these files will be saved in `all_files.txt`.

4. **Execution**: Run the Python script in your local environment, ensuring you have all necessary dependencies installed (`BeautifulSoup`, `urllib`, `selenium`, `webdriver`).

## How to Use

1. Ensure you have Python installed on your system.
2. Install the required dependencies using pip:
    ```bash
    pip install beautifulsoup4 urllib selenium
    ```
3. Download the geckodriver for Firefox and add its location to your system PATH.
4. Run the script and follow the on-screen instructions.

## Disclaimer

This script is intended for educational purposes and scraping GitHub may be subject to GitHub's usage policies.

---

