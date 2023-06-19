'''This script connects to a Redis database running locally on the host machine.'''
import os
import redis

# Retrieve the hostname and port from environment variables
hostname = os.getenv("HOSTNAME")
port = os.getenv("PORT")

# Connect to Redis using the hostname and port
r = redis.Redis(host=hostname, port=port) # type: ignore

# Perform operations on the Redis database
# For example, set a key-value pair
r.set("mykey", "myvalue")

# Retrieve the value for a given key
value = r.get("mykey")
print(value)
