import os
import urlparse
from redis import Redis
from rq import Worker, Queue, Connection


listen = ['high', 'default', 'low']

redis_url = os.getenv('REDISTOGO_URL')
urlparse.uses_netloc.append('redis')
url = urlparse.urlparse(redis_url)
conn = Redis(host=url.hostname, port=url.port, db=0, password=url.password)

#redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
#conn = Redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()


