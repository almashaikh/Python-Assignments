#this assignment is all about building my own reusable stopwatch which starts automatically when entering with "with" block & stops when
# leaving it even when an error happens inside of it

import time 
from contextlib import contextmanager

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.perf_counter() - self.start
        return False
    
class TimerData:
    """Simple object to store elapsed time."""
    pass

@contextmanager
def timer():
    t = TimerData()
    t.start = time.perf_counter()

    try:
        yield t
    finally:
        t.elapsed = time.perf_counter() - t.start

if __name__ == "__main__":

    print("Using the class-based context manager:")
    with Timer() as t:
        time.sleep(2)

    print(f"Elapsed time: {t.elapsed:.4f} seconds")

    print("\nUsing the contextlib-based context manager:")
    with timer() as t:
        time.sleep(1.5)

    print(f"Elapsed time: {t.elapsed:.4f} seconds")
