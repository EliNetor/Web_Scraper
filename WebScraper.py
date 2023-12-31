import httpx
from bs4 import BeautifulSoup
import asyncio

async def fetch_html(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text

async def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)

async def main():
    url = "https://www.ap.be"
    html_code = await fetch_html(url)
    await parse_html(html_code)

if __name__ == "__main__":
    asyncio.run(main())