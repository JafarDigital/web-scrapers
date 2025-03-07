from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import subprocess

# BeautifulSoup скрейпър
def scrape_with_beautifulsoup(url: str, element: str, class_name: str = None) -> str:
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        print(f"BeautifulSoup: GET {url} - Status Code: {response.status_code}")  # ✅ DEBUG

        soup = BeautifulSoup(response.content, "html.parser")

        if class_name and class_name.strip():
            # CSS селектор: напр. 'a.primary-link'
            elements = soup.select(f"{element}.{class_name.strip().replace(' ', '.')}")
        else:
            elements = soup.find_all(element)

        result = "\n".join([e.get_text(strip=True) for e in elements])
        print(f"📌 [DEBUG] BeautifulSoup Result: {result}")  # ✅ DEBUG

        return result if result else "⚠️ Няма намерени елементи."
    except Exception as e:
        return f"Error: {e}"

# Selenium скрейпър
def scrape_with_selenium(url: str, element: str, class_name: str = None) -> str:
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Стартира браузъра в headless режим
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        driver.get(url)
        driver.implicitly_wait(5)

        if class_name:
            elements = driver.find_elements(By.CLASS_NAME, class_name)
        else:
            elements = driver.find_elements(By.TAG_NAME, element)

        result = "\n".join([e.text.strip() for e in elements])
        print(f"Selenium Result: {result}")  # ✅ DEBUG

        driver.quit()
        return result if result else "⚠️ Няма намерени елементи."
    except Exception as e:
        return f"Error: {e}"

# Scrapy скрейпър (използване на subprocess)
def scrape_with_scrapy(url: str, element: str, class_name: str = None) -> str:
    try:
        result = subprocess.run(
            [
                "scrapy", "crawl", "example_spider",
                "-a", f"url={url}",
                "-a", f"element={element}",
                "-a", f"class_name={class_name if class_name else ''}"
            ],
            cwd="my_scraper",  # Важно! Стартираме от Scrapy папката
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()
        print(f"📌 [DEBUG] Scrapy Output: {output}")  # Debug

        return output if output else "⚠️ Няма намерени елементи."
    except Exception as e:
        return f"Error: {e}"
