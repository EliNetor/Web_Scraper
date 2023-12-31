import httpx
from bs4 import BeautifulSoup
import string

async def fetch_html(url):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()  
            return response.text
    except httpx.HTTPStatusError as exc:
        print(f"HTTP status error: {exc}")
        return None  
    except httpx.RequestError as exc:
        print(f"Request error: {exc}")
        return None  

async def getText(html):
    if html is None:
        return []
    
    soup = BeautifulSoup(html, 'html.parser')
    text_element = soup.find_all('p')
    all_texts = [element.get_text() for element in text_element]
    full_string = " ".join(all_texts)

    full_string = full_string.encode("ascii", "ignore").decode()

    translator = str.maketrans("", "", string.punctuation)
    full_string = full_string.translate(translator)

    words = full_string.split()

    word_amount = {}
    for word in words:
        x = full_string.count(word)
        word_amount.update({word:x})

    return word_amount

async def getA(html):
    if html is None:
        return []
    
    soup = BeautifulSoup(html, 'html.parser')
    url_element = soup.find_all('a')
    all_urls = [element.get('href') for element in url_element if element.get('href') and element.get('href').startswith('http')]
    return all_urls