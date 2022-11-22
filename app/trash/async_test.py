import asyncio
import aiohttp
import csv
import time


all_data = []


async def get_page_data(session, url):
    async with session.get(url) as resp:
        assert resp.status == 200
        print(f"getting url: {url}")
        resp_text = await resp.text()
        all_data.append(resp_text)
        return resp_text


async def load_site_data():
    async with aiohttp.ClientSession() as session:
        tasks = []
