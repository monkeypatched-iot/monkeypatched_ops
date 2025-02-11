# Use the official Redis stack image with RedisSearch module included
FROM redis/redis-stack:latest

# Expose the default Redis port
EXPOSE 6379

# Command to run Redis with required configurations
CMD ["redis-server", "--requirepass", "MyStrongPassword", "--bind", "0.0.0.0", "--loadmodule", "/opt/redis-stack/lib/redisearch.so"]