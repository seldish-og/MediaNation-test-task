import requests
import lxml
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class Parser:
    def __init__(self) -> None:
        user_agent = UserAgent()
        self.headers = {
            'User-Agent': user_agent.random
        }
        self.proxies = {
            'http': 'socks5://testvicky2:2a31eb@193.23.50.245:10490'
        }

    def get_page_content(self, url):
        response = requests.get(
            url=url, headers=self.headers, proxies=self.proxies
        )
        return response.content

    def parse_html(self, page_text):

        soup = BeautifulSoup(page_text, "lxml")

        creds = soup.find("h1", class_="page-title__title")

        return creds.text

    def get_content(self, url):
        try:
            page_text = self.get_page_content(url)
            creds = self.parse_html(page_text)
        except Exception as ex:
            print("Bad URl")
            raise requests.exceptions.InvalidURL
        return (creds, page_text)
