import asyncio
from nats.aio.client import Client as NATS

async def publish_message():
    nc = NATS()
    
    try:
        # Connect to the NATS server
        await nc.connect("nats://4.156.199.8:4222")

        # Publish a message
        subject = "updates"
        message = "Hello from Python!"
        await nc.publish(subject, message.encode())

        print(f"Published message to subject '{subject}': {message}")

        # Close the connection
        await nc.drain()
    except Exception as e:
        print(f"Error: {e}")

# Run the async function
asyncio.run(publish_message())
