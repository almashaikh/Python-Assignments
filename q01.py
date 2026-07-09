from typing import List, Dict
from collections import defaultdict
from itertools import groupby

def is_prime(n: int) -> bool:
    """Check if an integer is a prime number."""
    if n < 2:
        return False
    if n in (2,3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_category(n: int) -> str:
    """Determin the string category for a given number."""
    if n % 2 == 0:
        return "even"
    if is_prime(n):
        return "odd_prime"
    return "odd_not_prime"

def group_standard(numbers: List[int]) -> Dict[str, List[int]]:
    result: Dict[str, List[int]] = {"even": [], "odd_prime": [], "odd_not_prime": []}

    for n in numbers:
        result[get_category(n)].append(n)

    return result

def group_defaultdict(numbers: List[int]) -> Dict[str, List[int]]:
    result: defaultdict[str, List[int]] = defaultdict(list)
    
    for n in numbers:
        result[get_category(n)].append(n)
        
    return dict(result)

def group_itertools(numbers: List[int]) -> Dict[str, List[int]]:
    # I would pick groupby when processing large, memory-heavy data streams that are already sorted, since it acts as a lazy iterator.
    sorted_numbers = sorted(numbers, key=get_category)
    result: Dict[str, List[int]] = {}
    
    for key, group in groupby(sorted_numbers, key=get_category):
        result[key] = list(group)
        
    return result

if __name__ == "__main__":
    test_input = [1,2,3,4,5,6,9,11]
    expected_output = {"even": [2, 4, 6], "odd_prime": [3, 5, 11], "odd_not_prime": [1, 9]}
    print("Executing manual test cases")

    print("Standard Dict Result:")
    res_standard = group_standard(test_input)
    print(res_standard)

    print("\nDefaultDict Result:")
    res_defaultdict = group_defaultdict(test_input)
    print(res_defaultdict)

    print("\nItertools Groupby Result:")
    res_itertools = group_itertools(test_input)
    print(res_itertools)

    assert res_standard == expected_output, "Standard dict test failed!"
    assert res_defaultdict == expected_output, "Defaultdict test failed!"
    assert res_itertools == expected_output, "Groupby test failed!"

    print("\nAll test cases passed successfully!")