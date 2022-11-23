import time
import threading
import requests
from parser import Parser
from data import File, Index


parser = Parser()
file = File()
index = Index()


def make_result(url):
    try:
        creds, html = parser.get_content(url=url)
        file.write_results(url=url, creds=creds, html=html)
    except requests.exceptions.InvalidURL as url_ex:
        pass


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
