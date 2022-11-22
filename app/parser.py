import requests
import lxml
from bs4 import BeautifulSoup


class Parser:
    def __init__(self) -> None:
        pass

    def get_page_content(self, url):
        response = requests.get(url)
        return response.content

    def parse_html(self, page_text):

        soup = BeautifulSoup(page_text, "lxml")

        creds = soup.find("h1", class_="page-title__title")

        return creds.text

    def get_content(self, url):
        page_text = self.get_page_content(url)
        creds = self.parse_html(page_text)
        return (creds, page_text)
