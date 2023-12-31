import httpx
from bs4 import BeautifulSoup

async def fetch_html(url):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
            return response.text
    except httpx.HTTPStatusError as exc:
        print(f"HTTP status error: {exc}")
        return None  # Return None in case of an error
    except httpx.RequestError as exc:
        print(f"Request error: {exc}")
        return None  # Return None in case of an error

async def getText(html):
    if html is None:
        return []
    
    soup = BeautifulSoup(html, 'html.parser')
    text_element = soup.find_all('p')
    all_texts = [element.get_text() for element in text_element]
    return all_texts

async def getA(html):
    if html is None:
        return []
    
    soup = BeautifulSoup(html, 'html.parser')
    url_element = soup.find_all('a')
    all_urls = [element.get('href') for element in url_element if element.get('href') and element.get('href').startswith('http')]
    return all_urls