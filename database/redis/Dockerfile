# Use the official Redis stack image with RedisSearch module included
FROM redis/redis-stack:latest

# Expose the default Redis port
EXPOSE 6379

# Command to run Redis
CMD ["redis-server", "--loadmodule", "/opt/redis-stack/lib/redisearch.so"]
