# Web Scrapers with FastAPI

## • Overview  
This project is a **FastAPI-based web scraper** that allows users to extract HTML elements from websites using:  
- **BeautifulSoup**  
- **Selenium**
- **Honourable mention:** attempted web-scraping with Scrapy for the first time  

## • Features  
- Web-based interface 
- Select a scraper (**BeautifulSoup** or **Selenium**; Scrapy not guaranteed to work)  
- Scrape elements (`div`, `p`, `a`, etc.)  
- Specify class names to filter results - field not required to fill  

## • Installation  

### 1. Clone the Repository  

### 2. Create a Virtual Environment

### 3. Install Dependencies using requirements.txt

### 4. Run the FastAPI Server

  uvicorn app.main:app --reload

### 5. Access the Web Interface
Open http://127.0.0.1:8000

## • Technologies Used
Python 3, 
FastAPI, 
BeautifulSoup, 
Selenium, 
Jinja2 for HTML Templates

## • Scrapy - Honorable Mention
While this project primarily utilizes BeautifulSoup and Selenium, I initially attempted to integrate Scrapy for a more structured, scalable scraping solution. After troubleshooting various issues, I managed to scrape a news website, but Scrapy's asynchronous nature and setup complexity made it less practical for this project’s scope.

For this reason, Scrapy remains available in the form selection as an "honorable mention", though it may not work as expected without additional configuration in the scapers.py script. Feel free to experiment with it!
