import httpx
from bs4 import BeautifulSoup
import asyncio
import string

async def fetch_html(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text

async def getText(html):
    soup = BeautifulSoup(html, 'html.parser')
    text_element = soup.find_all('p')
    all_texts = [element.get_text() for element in text_element]
    return all_texts

async def getA(html):
    soup = BeautifulSoup(html, 'html.parser')
    url_element = soup.find_all('a')
    all_urls = [element.get('href') for element in url_element if element.get('href') and element.get('href').startswith('http')]
    return all_urls

async def main():
    url = "https://www.ap.be"
    html_code = await fetch_html(url)
    all_p = await getText(html_code)
    full_string = " ".join(all_p)

    translator = str.maketrans("", "", string.punctuation)
    full_string = full_string.translate(translator)

    words = full_string.split()

    word_amount = {}
    for word in words:
        x = full_string.count(word)
        word_amount.update({word:x})
    
    print(word_amount)
    print( await getA(html_code))

if __name__ == "__main__":
    asyncio.run(main())