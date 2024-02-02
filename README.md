# Article-Reader-App

This Python script is designed to extract structured data from various news articles. It utilizes web scraping techniques to extract information such as article titles and bodies from different news websites. The script supports multiple websites, and you can easily extend it to include more by adding functions for each website.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Prerequisites

- Python 3.x
- Required Python libraries (install via `pip install -r requirements.txt`):
  - `requests`
  - `bs4`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/NotShrirang/Article-Reader-App
   ```

2. Navigate to the project directory:
   
  ```bash
  cd Article-Reader-App
  ```

3. Install the required dependencies:

  ```bash
  pip install -r requirements.txt
  ```
## Usage

Edit the config.json file to configure the list of news article URLs.

Run the main script:

```bash
python main.py
```
The extracted data will be saved as output.json in the project directory.

## Configuration
config.json: This file contains the configuration for the script. It includes a list of news article URLs that you want to extract data from. Add or remove URLs as needed.
