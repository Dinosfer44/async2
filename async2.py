import asyncio
import random

async def print_message(message, delay):
    await asyncio.sleep(delay)
    print (message)

async def main():
    messages = ["Привет!", "Как дела?", "До свидания!"]
    tasks = [print_message(msg, random.uniform(0, 2)) for msg in messages]
    await asyncio.gather(*tasks)

asyncio.run(main())