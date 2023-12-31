import httpx
from bs4 import BeautifulSoup
import asyncio
import string
import functions as f
import classes

async def async_main(crawler):
    # je zal per pagina die je wil crawlen ook een task moeten maken
    # lees de documentatie van create_task!
    task = asyncio.create_task(crawler.crawl(crawler.initial_page, 0))
    crawler.background_tasks.add(task)
    task.add_done_callback(crawler.background_tasks.discard)
    # moet met while lus
    # wachten op taken genereert nieuwe taken
    # we willen dat de main pas eindigt als alle gegenereerde taken klaar zijn
    while crawler.background_tasks:
        await asyncio.gather(*crawler.background_tasks)

async def main():
    visited_links = set()
    initial_page_url = "https://www.ap.be/"
    max_crawl_depth = 2

    crawler = classes.Crawler(visited_links, initial_page_url, max_crawl_depth)
    await async_main(crawler)


if __name__ == "__main__":
    asyncio.run(main())