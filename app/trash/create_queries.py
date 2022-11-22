import redis
import time
import csv


class Query:
    def __init__(self) -> None:
        pool = redis.ConnectionPool(host='localhost', port=16379, db=0)
        self.redis = redis.Redis(connection_pool=pool)

    def get_urls(self):
        urls = []
        with open("files/habr.csv") as csv_file:
            csv_rows = csv.reader(csv_file, delimiter=' ')
            for row in csv_rows:
                urls.append(''.join(row))
        return urls

    def create_queries(self):
        if not self.redis.lrange('urls', 0, 1):
            urls = self.get_urls()
            for url in urls:
                self.redis.rpush('urls', url)
                print("adding queries")


q = Query()
# print(q.create_queries())
# q.redis.flushdb()
