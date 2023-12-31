import functions as f
import asyncio

class Crawler:
    def __init__(self, visited, initial_page, max_depth):
        self.max_depth = max_depth
        self.initial_page = initial_page
        self.visited = visited
        self.background_tasks = set()

    async def crawl(self, starting_link, depth):
        if depth > self.max_depth or starting_link in self.visited:
            return
        
        self.visited.add(starting_link)

        html_code = await f.fetch_html(starting_link)
        links = await f.getA(html_code)

        print(f"Starting link = {starting_link}, links in starting link: {links}")

        tasks = []
        for link in links:
            task = asyncio.create_task(self.crawl(link,depth + 1))
            self.background_tasks.add(task)
            task.add_done_callback(self.background_tasks.discard)
            tasks.append(task)

        await asyncio.gather(*tasks)

        
            # dit vul je zelf aan
            # je zal hier ook create_task nodig hebben
            # opnieuw: lees die documentatie


            # dit vul je zelf aan
            # je zal hier ook create_task nodig hebben
            # opnieuw: lees die documentatie