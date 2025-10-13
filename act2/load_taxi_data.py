# Do not run this example in Jupyter as it has some special handling of the event loop, asyncio.run() would fail.
# Install pandas and fastparquet in venv before running it.
import asyncio
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import time
import sys
from itertools import cycle


def load_taxi_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Mostly IO-Bound blocking operations"""
    # NY yellow taxi trips Jan 2023
    url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"
    print("Loading dataset...")
    df = pd.read_parquet(url, engine="fastparquet")
    print("Dataset loaded:", df.shape)

    # NY taxi zones data
    zones_url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv"
    zones = pd.read_csv(zones_url)
    return df, zones


def trips_data_by_borough(trips: pd.DataFrame, zones: pd.DataFrame) -> pd.DataFrame:
    """CPU-Bound blocking operations"""
    start = time.time()

    # Join trips with zone data
    merged = trips.merge(zones, left_on="PULocationID", right_on="LocationID", how="left")

    # GroupBy by Borough sort
    agg = (
        merged.groupby("Borough")
        .agg(
            total_trips=("VendorID", "count"),
            avg_distance=("trip_distance", "mean"),
            avg_fare=("fare_amount", "mean"),
        )
        .sort_values("total_trips", ascending=False)
    )

    print("Execution time:", time.time() - start, "seconds")
    return agg


def sync_code() -> pd.DataFrame:
    trips, zones = load_taxi_data()
    res = trips_data_by_borough(trips, zones)
    return res


async def call_sync_code(done: asyncio.Event) -> pd.DataFrame:
    # FIXME: Make the call to sync_code non-blocking so spinner can run concurrently displaying
    # the spinner at all times.
    # Notice both_taxi_data() and trips_data_by_borough() will block the spinner in this implementation.
    # See `run_in_executor()` function, pick the most appropiate executor for maximum concurrency.
    # Find a video of how the spinner should look like attached.
    loop = asyncio.get_running_loop()

    # Using a ThreadPoolExecutor (for I/O-bound tasks)
    with ThreadPoolExecutor() as thread_pool:
        res = await loop.run_in_executor(thread_pool, sync_code)
    done.set()
    return res


async def spinner(done: asyncio.Event) -> None:
    symbols = cycle("/-\\|")
    print()
    for symbol in symbols:
        if done.is_set():
            break
        sys.stdout.write(f"\033[3D[{symbol}]")
        sys.stdout.flush()
        await asyncio.sleep(0.3)
    print("X")


async def main() -> None:
    done = asyncio.Event()
    result, _ = await asyncio.gather(call_sync_code(done), spinner(done))
    print(f"{result=}")


asyncio.run(main())