# redis_client.py
import redis

# Connect to Redis server
client = redis.Redis(host='localhost', port=6379, db=0)

def get_redis_client():
    return client