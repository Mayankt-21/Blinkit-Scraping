# Blinkit Data Scraper

A Python-based web scraping tool for collecting product data from Blinkit's website across different categories and locations.

## Project Structure

- `main.py` - Entry point of the application
- `my_scrapper.py` - Core scraping functionality using Selenium  
- `data.py` - Data loading utilities
- `pretty_data.py` - Data processing and formatting
- `test.py` - Manual testing script

## Prerequisites

- Python 3.10+
- Chrome browser installed 
- Virtual environment (recommended)

## Installation

1. Clone the repository
2. Create and activate virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate
```
3. Install required packages:
```bash
pip install -r requirements.txt
```

## Configuration

Place your input data files in the `datasets` folder:

- `blinkit_categories.csv` - Category information
- `blinkit_locations.csv` - Location coordinates

## Usage

Run the main script:
```bash
python main.py
```

For testing with sample data:
```bash
python test.py
```

**Note**: A complete scraping session typically takes 30-40 minutes depending on the number of categories and locations here considered for 120-150.

## Features

- Automated data collection from Blinkit
- Location spoofing support
- Category-wise product scraping
- Detailed product information extraction
- Rate limiting with configurable delays
- Error handling and retries
- CSV output generation

## Output

The scraper generates `final_output.csv` containing:

- Product details
- Category information
- Pricing data
- Inventory status
- Timestamps, etc

## Technical Notes

- Uses Selenium WebDriver with Chrome in headless mode
- Implements geolocation spoofing
- Handles pagination and dynamic content
- Includes retry mechanism for failed requests
- Supports concurrent scraping across multiple categories and locations
