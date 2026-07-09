from typing import List, Tuple

# Type alias for clean type hinting
RecordType = Tuple[str, int, float]

def sort_records(records: List[RecordType]) -> List[RecordType]:
    # We return a tuple for the key. 
    # Python sorts tuples item by item. 
    # -x[2] sorts score descending (e.g., -92.5 comes before -88.0).
    # x[1] sorts joining_order ascending as the tie-breaker.
    return sorted(records, key=lambda x: (-x[2], x[1]))

if __name__ == "__main__":
    records_data: List[RecordType] = [
        ("asha", 3, 92.5), 
        ("ravi", 1, 92.5), 
        ("meera", 2, 88.0)
    ]
    
    expected_output = [
        ("ravi", 1, 92.5), 
        ("asha", 3, 92.5), 
        ("meera", 2, 88.0)
    ]

    print("Original Records:")
    for r in records_data:
        print(r)
        
    result = sort_records(records_data)
    
    print("\nSorted Records:")
    for r in result:
        print(r)

    assert result == expected_output, "Sort order is incorrect!"
    print("\nTest passed successfully!")