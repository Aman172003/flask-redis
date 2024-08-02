import redis

# Connect to the Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Set a key-value pair
r.set('mykey', 'Hello, Redis!')

# Get the value of a key
print(r.get('mykey'))  # Will print b'Hello, Redis!'
