import csv
import redis


class File:
    def __init__(self) -> None:
        pass

    def get_urls(self):
        urls = []
        with open("files/urls/test.csv") as csv_file:
            csv_rows = csv.reader(csv_file, delimiter=' ')
            for row in csv_rows:
                urls.append(''.join(row))
        return urls

    # на интервью было утчнено что сохранять именно в .html разрешении
    def write_results(self, url, creds, html):
        with open("files/results/{}.html".format(creds.replace(' ', '')), "w") as file:
            result = "{}\n{}\n{}\n".format(url, creds, html)
            file.write(result)


class Index:
    def __init__(self) -> None:
        pool = redis.ConnectionPool(host='localhost', port=16379, db=0)
        self.redis = redis.Redis(connection_pool=pool)

    def update_index(self, num):
        old_index = int(self.redis.get("last_index"))
        self.redis.set("last_index", old_index + num)

    def reset_redis(self):
        self.redis.flushdb()

    def get_last_index(self):
        if not self.redis.get("last_index"):
            self.redis.set("last_index", 1)

        last_index = self.redis.get("last_index")
        return last_index
