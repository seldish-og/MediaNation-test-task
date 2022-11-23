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


def make_threads(first_url, second_url):
    thread1 = threading.Thread(target=make_result, args=(first_url,))
    thread2 = threading.Thread(target=make_result, args=(second_url,))

    thread1.start()
    thread2.start()


def main():
    urls = file.get_urls()
    last_index = int(index.get_last_index())

    print(f"-----LAST INDEX IS: {last_index}-----")

    for i in range(last_index, len(urls) - 1, 2):
        first_url = urls[i]
        second_url = urls[i + 1]

        print(first_url, second_url)
        make_threads(first_url, second_url)
        index.update_index(2)

    index.reset_redis()


if __name__ == "__main__":
    main()
