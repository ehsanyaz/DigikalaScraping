# Digikala Web Scarping Using PlayWright Asynco

from bs4 import BeautifulSoup
import asyncio

from playwright.async_api import async_playwright

async def func():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page()
        url = "https://www.digikala.com/search/category-book/"
        await page.goto(url)
        await page.wait_for_selector('h3')
        return await page.content()


html = asyncio.run(func())
soup = BeautifulSoup(html,"html.parser")
divs = soup.find_all("div",attrs = {"class":"product-list_ProductList__item__LiiNI"})
for div in divs:
    print(div)
    div_soup = BeautifulSoup(div,"html.parser")
