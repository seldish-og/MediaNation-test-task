import time
import threading
from parser import Parser
from data import File, Index


parser = Parser()
file = File()
index = Index()


def make_result(url):
    creds, html = parser.get_content(url=url)
    file.write_results(url=url, creds=creds, html=html)


def make_threads(first_url, second_url):
    thread1 = threading.Thread(target=make_result, args=(first_url,))
    thread2 = threading.Thread(target=make_result, args=(second_url,))

    thread1.start()
    thread2.start()


def main():
    urls = file.get_urls()
    last_index = int(index.get_last_index())

    for url in urls[last_index:]:
        url_index = urls.index(url)

        first_url = urls.pop(url_index)
        second_url = urls.pop(url_index + 1)
        make_threads(first_url, second_url)
        index.update_index(2)

    index.reset_redis()

# results = parser.get_content(url)
# data.write_results(url=url, creds=results[0], html=results[1])

# def main():
#     last_inex1, last_index2 = get_indexes()
#     thread1 = threading.Thread(target=parse)
#     thread2 = threading.Thread(target=parse)

#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()


if __name__ == "__main__":
    main()
