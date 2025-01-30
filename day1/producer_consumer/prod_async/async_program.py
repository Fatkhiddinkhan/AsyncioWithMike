import asyncio
import datetime
import colorama
import random
import time

def main():
    loop = asyncio.get_event_loop()

    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + "App started.", flush=True)

    data = asyncio.Queue()

    task1 = loop.create_task(generate_data(30, data))
    task2 = loop.create_task(process_data(20, data))
    task3 = loop.create_task(process_data(40, data))

    loop.run_until_complete(asyncio.gather(task1, task2))
    dt = datetime.datetime.now() - t0
    print(colorama.Fore.WHITE + f"App exiting, total time: {dt.total_seconds():,.2f} sec.", flush=True)


async def generate_data(num: int, data: asyncio.Queue):
    for idx in range(1, num + 1):
        item = idx * idx
        print(colorama.Fore.YELLOW + f"(awaiting) Putting item {item} into queue...", flush=True)
        await data.put((item, datetime.datetime.now()))
        print(colorama.Fore.GREEN + f"(done) Item {item} added to queue.", flush=True)

        print(colorama.Fore.YELLOW + f"(awaiting) Sleeping before generating next item...", flush=True)
        await asyncio.sleep(random.random() + .5)
        print(colorama.Fore.GREEN + "(done) Wake up from sleep.1", flush=True)


async def process_data(num: int, data: asyncio.Queue):
    processed = 0
    while processed < num:
        print(colorama.Fore.CYAN + "(awaiting) Waiting to get item from queue...", flush=True)
        item = await data.get()
        print(colorama.Fore.GREEN + f"(done) Got item {item[0]} from queue.", flush=True)

        processed += 1
        value = item[0]
        t = item[1]
        dt = datetime.datetime.now() - t

        print(colorama.Fore.CYAN +
              f" +++ Processed value {value} after {dt.total_seconds():,.2f} sec.", flush=True)
        print(colorama.Fore.YELLOW + "(awaiting) Sleeping before processing next item...", flush=True)
        await asyncio.sleep(.5)
        print(colorama.Fore.GREEN + "(done) Wake up from sleep.2", flush=True)


if __name__ == '__main__':
    main()
