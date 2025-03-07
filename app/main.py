from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.scraper import scrape_with_beautifulsoup, scrape_with_selenium, scrape_with_scrapy

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/scrape", response_class=HTMLResponse)
async def scrape_form(
    request: Request,
    url: str = Form(...),
    element: str = Form(...),
    class_name: str = Form(None),
    scraper: str = Form(...)
):
    if scraper == "beautifulsoup":
        result = scrape_with_beautifulsoup(url, element, class_name)
    elif scraper == "selenium":
        result = scrape_with_selenium(url, element, class_name)
    elif scraper == "scrapy":
        result = scrape_with_scrapy(url, element, class_name)
    else:
        result = "⚠️ Невалиден избор на скрейпър."

    print(f"📌 [DEBUG] Резултат: {result}")  # ✅ DEBUG в терминала

    return templates.TemplateResponse("result.html", {"request": request, "result": result})
