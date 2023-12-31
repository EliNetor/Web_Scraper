import functions as f
import asyncio
import json

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

        json_file = 'data.json'

        html_code = await f.fetch_html(starting_link)
        links = await f.getA(html_code)

        # print(f"Starting link = {starting_link}, links in starting link: {links}")

        new_data ={ 
            "Redirects":links
        }

        try:
            with open(json_file, 'r') as json_f:
                data = json.load(json_f)
        except FileNotFoundError:
            data = {}

        data[starting_link] = new_data

        with open(json_file,'w') as json_f:
            json.dump(data, json_f, indent=3)

        tasks = []
        for link in links:
            task = asyncio.create_task(self.crawl(link,depth + 1))
            self.background_tasks.add(task)
            task.add_done_callback(self.background_tasks.discard)
            tasks.append(task)

        await asyncio.gather(*tasks)
