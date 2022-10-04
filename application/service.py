import asyncio
from typing import List

import requests
from starlette import status


class Service:

    def collect_cat_facts(self) -> List[str]:
        url = "https://cat-fact.herokuapp.com/facts/random?amount=1"
        loop = asyncio.new_event_loop()
        tasks = [
            asyncio.ensure_future(self.call_api(url), loop=loop) for _ in range(5)
        ]
        return [text for text in loop.run_until_complete(asyncio.gather(*tasks))]

    @staticmethod
    async def call_api(url: str) -> str:
        response = requests.get(url)
        assert response.status_code == status.HTTP_200_OK
        return response.json()["text"]
