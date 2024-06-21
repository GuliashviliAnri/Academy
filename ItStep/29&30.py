import asyncio
import time

async def start():
    print("Completed")
    await asyncio.sleep(1)
    return


async def end():
    print("Starting...")
    time.sleep(4)
    await start()


asyncio.run(end())






