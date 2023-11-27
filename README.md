# Metacritic 'Must-See' Movies Scraper

## Overview
This Python script is designed to scrape 'must-see' movie titles from the Mystery (Change the url for other categories) category on Metacritic. It targets movies based on user scores and specifically extracts titles tagged as 'must-see'.

## Features
- Scrapes the first two pages of the 'Mystery' category on Metacritic for 'must-see' movies.
- Extracts movie titles and presents them in a user-friendly format.
- Handles basic network errors and server response validations.

## Prerequisites
Before running the script, ensure that you have the following installed:
- Python 3.x
- Requests library
- BeautifulSoup4 library

## Installation
1. Clone this repository or download the script to your local machine.
2. Install the necessary Python libraries. Open a terminal and run:
   ```bash
   pip install requests beautifulsoup4
