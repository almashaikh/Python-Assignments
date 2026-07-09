from typing import Any

def run_snippet_1() -> None:
    print("--- Snippet 1 ---")
    a, *b, c = [1, 2, 3, 4, 5]
    print(a, b, c)

def run_snippet_2() -> None:
    print("\n--- Snippet 2 ---")
    first, second = {"x": 1, "y": 2}
    print(first, second)

def run_snippet_3() -> None:
    print("\n--- Snippet 3 ---")
    
    def f(*args: Any, **kwargs: Any) -> None:
        print(args, kwargs)
        
    f(1, 2, key="val")
    f(*[1, 2], **{"key": "val"})

def run_snippet_4() -> None:
    print("\n--- Snippet 4 ---")
    # Disabling the linter warning for this specific line since 
    # the chained assignment is the deliberate point of the question.
    x, y = y, x = 1, 2  # noqa
    print(x, y)

if __name__ == "__main__":
    run_snippet_1()
    run_snippet_2()
    run_snippet_3()
    run_snippet_4()