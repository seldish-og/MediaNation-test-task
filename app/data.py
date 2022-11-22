import csv
import redis


class Data:
    def __init__(self) -> None:
        pool = redis.ConnectionPool(host='localhost', port=16379, db=0)
        self.redis = redis.Redis(connection_pool=pool)

    def get_urls(self):
        urls = []
        with open("files/urls/habr.csv") as csv_file:
            csv_rows = csv.reader(csv_file, delimiter=' ')
            for row in csv_rows:
                urls.append(''.join(row))
        return urls

    def write_result_file(self, url, creds, html):
        pass

    def set_new_index(self):
        pass

    def get_last_indexes(self):
        index1 = self.redis.get("index1")
        index2 = self.redis.get("index2")
        return index1, index2
