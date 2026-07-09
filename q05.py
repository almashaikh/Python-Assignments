from typing import List, Optional

def append_to_original(item: int, target: List[int] = []) -> List[int]:
    target.append(item)
    return target

def append_to_fixed(item: int, target: Optional[List[int]] = None) -> List[int]:
    if target is None:
        target = []
    target.append(item)
    return target

if __name__ == "__main__":
    print("---Original Output (The trap) ---")
    print(append_to_original(1))
    print(append_to_original(2))
    print(append_to_original(3,[]))
    print(append_to_original(4))

    print("\n--- Fixed Output ---")
    print(append_to_fixed(1))
    print(append_to_fixed(2))
    print(append_to_fixed(3, []))
    print(append_to_fixed(4))