import asyncio
import time

async def task_one():
    """An asynchronous task that prints a message and sleeps."""
    print("Task One: Starting...")
    await asyncio.sleep(2) # Simulate some I/O-bound operation
    print("Task One: Finished!")

async def task_two():
    """Another asynchronous task that prints a message and sleeps."""
    print("Task Two: Starting...")
    await asyncio.sleep(1) # Simulate another I/O-bound operation
    print("Task Two: Finished!")

async def main():
    """The main coroutine to run the asynchronous tasks concurrently."""
    print("Main: Creating tasks...")
    # Create tasks to run concurrently
    start_time = time.time()
    await asyncio.gather(task_one(), task_two())
    print(f"Main: All tasks completed in {time.time() - start_time}.")

if __name__ == "__main__":
    asyncio.run(main())
