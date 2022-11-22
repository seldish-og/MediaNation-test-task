import asyncio
import aiohttp
import csv
import time
import threading
import requests


def parse():
    r = requests.get(url)
    print(r.text)


def main():
    thread1 = threading.Thread(target=parse)
    thread2 = threading.Thread(target=parse)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
