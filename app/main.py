import time
import threading
import requests
from parser import Parser
from data import File, Redis_db


parser = Parser()
file = File()
redis_db = Redis_db()


def make_result(url):
    try:
        creds, html = parser.get_content(url=url)
        file.write_results(url=url, creds=creds, html=html)
    except requests.exceptions.InvalidURL as url_ex:
        redis_db.update_bad_urls(url=url)


def make_threads(first_url, second_url):
    thread1 = threading.Thread(target=make_result, args=(first_url,))
    thread2 = threading.Thread(target=make_result, args=(second_url,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


def main():
    urls = file.get_urls()
    last_index = int(redis_db.get_last_index())

    print(f"-----LAST INDEX IS: {last_index}-----")
    last_url = urls[-1]
    for i in range(last_index, len(urls) - 1, 2):
        first_url = urls[i]
        second_url = urls[i + 1]

        print(f"PARSING: {first_url}---", f"---PARSING2: {second_url}")

        make_threads(first_url, second_url)
        redis_db.update_index(2)
    make_result(last_url)

    redis_db.write_bad_urls()
    redis_db.reset_redis()


if __name__ == "__main__":
    main()
