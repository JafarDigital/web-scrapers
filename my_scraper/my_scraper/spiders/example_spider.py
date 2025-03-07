import scrapy

class ExampleSpider(scrapy.Spider):
    name = "example_spider"

    def __init__(self, url=None, element=None, class_name=None, *args, **kwargs):
        super(ExampleSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url]
        self.element = element
        self.class_name = class_name

    def parse(self, response):
        self.log(f"📌 [DEBUG] Scraping URL: {response.url}")
        self.log(f"📌 [DEBUG] Looking for: <{self.element} class='{self.class_name}'>")

        # ✅ DEBUG: Запазва целия HTML, който Scrapy вижда
        with open("scraped_page.html", "w", encoding="utf-8") as f:
            f.write(response.text)

        # Проверяваме дали class_name е зададен
        if self.class_name:
            elements = response.css(f"{self.element}.{self.class_name}::text").getall()
        else:
            elements = response.css(f"{self.element}::text").getall()

        if elements:
            self.log(f"📌 [DEBUG] Found Elements: {elements}")
            yield {"results": elements}
        else:
            self.log(f"⚠️ [DEBUG] No elements found!")
            yield {"results": "⚠️ Няма намерени елементи."}
