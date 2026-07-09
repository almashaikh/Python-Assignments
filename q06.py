from typing import Iterable, Iterator, TypeVar
from itertools import islice

T = TypeVar('T')

def run_iterator_prediction() -> None:
    print("--- Iterator Prediction ---")
    nums = [1,2,3]
    it = iter(nums)

    print(2 in it)
    print(2 in it)
    print(list(it))

def chunks(iterable: Iterable[T], size: int) -> Iterator[list[T]]:
    iterator = iter(iterable)

    while True:
        chunk = list(islice(iterator, size))

        if not chunk:
            break

        yield chunk

if __name__ == "__main__":
    run_iterator_prediction()

    print("\n--- Chunks Generator ---")
    result = list(chunks(range(7), 3))
    print(result)

    assert result == [[0,1,2], [3,4,5], [6]], "Chunking failed"
    print("Generator test passed successfully")