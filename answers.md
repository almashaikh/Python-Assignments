# Q2: The Unpacking Circus

## Snippet 1: Star Unpacking
**Predicted Output:** `1 [2, 3, 4] 5`
* **The Mechanics:** This uses Python's extended iterable unpacking (PEP 3132). Python assigns the first mandatory variable (`a`) to the first element, and the last mandatory variable (`c`) to the last element. The `*b` acts as a catch-all, gathering all remaining unassigned elements into a new list.

## Snippet 2: Dictionary Unpacking
**Predicted Output:** `x y`
* **The Mechanics:** When Python unpacks an iterable, it uses the object's default iterator. The default iterator for a `dict` yields its keys, not its values. To get the values, you would have to explicitly call `.values()` or `.items()`.

## Snippet 3: The Packing and Unpacking Zippers
**Predicted Output:** `(1, 2) {'key': 'val'}`
`(1, 2) {'key': 'val'}`
* **The Mechanics:** * In the function signature `def f(*args, **kwargs)`, `*args` packs positional arguments into a tuple, and `**kwargs` packs keyword arguments into a dictionary. 
    * In the first call `f(1, 2, key="val")`, Python naturally packs the inputs.
    * In the second call `f(*[1, 2], **{"key": "val"})`, we use the operators to *unpack* the list and dictionary into raw positional and keyword arguments before they enter the function. The function then packs them right back up, resulting in the exact same output.

## Snippet 4: Chained Assignment Trap
**Predicted Output:** `2 1` *(This is the biggest surprise!)*
* **The Mechanics:** In chained assignments (`target1 = target2 = expression`), Python evaluates the expression on the far right exactly once, creating the tuple `(1, 2)`. It then assigns this tuple to the targets from **left to right**.
    1. First, `x, y = (1, 2)` evaluates. `x` becomes `1` and `y` becomes `2`.
    2. Next, `y, x = (1, 2)` evaluates. `y` becomes `1` and `x` becomes `2`.
    3. The final state leaves `x` as `2` and `y` as `1`.


# Q3: Comprehension Inception

## 1. Flat Sorted List of Unique Skills
**Expression:** `sorted({skill for members in teams.values() for member in members for skill in member["skills"]})`
* **The Mechanics:** In Python comprehensions, you read the `for` loops from left to right, exactly as they would be nested top-to-bottom in standard code. 
    1. `for members in teams.values()` (gets the list of dictionaries)
    2. `for member in members` (gets a specific employee's dictionary)
    3. `for skill in member["skills"]` (iterates over their skill list)
    4. `skill` (the final output placed into the set)

## 2. Dictionary of `{member_name: team_name}`
**Expression:** `{member["name"]: team for team, members in teams.items() for member in members}`
* **The Mechanics:** This requires a double-nested loop in a dict comprehension. 
    1. `for team, members in teams.items()` extracts both the key (`"backend"`) and the list of employees.
    2. `for member in members` iterates through the employees.
    3. `{member["name"]: team}` sets the output format as `Key: Value`.

## 3. Dictionary of `{team_name: member_count}` (Filtered)
**Expression:** `{team: len(members) for team, members in teams.items() if len(members) > 1}`
* **The Mechanics:** This demonstrates comprehension filtering. The `if len(members) > 1` acts as a gatekeeper at the very end of the expression. If the condition is `False`, the key-value pair `{team: len(members)}` is simply never evaluated or added to the resulting dictionary.


# Q4: Sort of Tricky

## What is a "Stable" Sort?
* **The Mechanics:** Python uses an algorithm called Timsort, which is guaranteed to be stable. This means that if two elements have the exact same key in a sorting operation, their original relative order from the input list is perfectly preserved in the output list.

## Solving with Two Consecutive `sorted()` Calls
Because Python's sort is stable, you can achieve complex multi-level sorting without fancy lambda math by sorting multiple times in **reverse order of priority**. 

To sort by Score (Descending) with a tie-breaker of Joining Order (Ascending), you sort the tie-breaker first, and the primary metric last:

1. **Pass 1 (Secondary Tie-Breaker):** `step1 = sorted(records, key=lambda x: x[1])`
   *This sorts everyone purely by joining order ascending.*

2. **Pass 2 (Primary Metric):**
   `final_result = sorted(step1, key=lambda x: x[2], reverse=True)`
   *This sorts the list by score descending. Because the sort is stable, when it sees that "asha" and "ravi" both have a score of 92.5, it refuses to swap their positions. It leaves them in the exact order they were already in from Pass 1 (where "ravi" (1) was placed before "asha" (3)).*


## Q5: Something Fishy Here

### Output Prediction
```text
[1]
[1, 2]
[3]
[1, 2, 4]

When is a def line's default value evaluated? Default parameter values are evaluated exactly once, from left to right, when the function definition is executed.

Link: Python Language Reference: Section 8.7 - Function Definitions

## Q6: Iterators vs. Iterables

--- Iterator Prediction ---
True
False
[]

--- Chunks Generator ---
[[0, 1, 2], [3, 4, 5], [6]]

 ## Q.7 Pending

 ## Q.8 

 ### Q1. If the block raises an exception, does your `__exit__` still run?

Yes. The `__exit__` method is always executed when leaving the `with` block, even if an exception occurs. This ensures that cleanup tasks (such as closing files, releasing resources, or measuring elapsed time) are always performed.

### Q2. What does returning `True` from `__exit__` do?

Returning `True` tells Python that the exception has been handled, so it suppresses the exception and prevents it from being propagated further.

If `__exit__` returns `False` (or `None`), Python re-raises the exception after `__exit__` finishes executing.

##Q.9

-----------

##Q.10

### Q. What does random.shuffle() require of its argument?
random.shuffle() requires a mutable sequence. It must support getting items by index, assigning items by index, and reporting its length so that elements can be swapped during shuffling.

### Q. How did you find out?
I referred to the Python standard library documentation for the random module, which states that random.shuffle() shuffles a mutable sequence in place. From this requirement, I implemented the necessary special methods (__len__, __getitem__, and __setitem__) in the Deck class.


###Q.11



### Q.12
### Q1. When do `try`, `except`, `else`, and `finally` run?

- **try:** Runs first and contains the code that may raise an exception.
- **except:** Runs only if an exception matching the specified type is raised in the `try` block.
- **else:** Runs only if the `try` block completes successfully without raising any exceptions.
- **finally:** Always runs after the `try`, `except`, or `else` blocks, regardless of whether an exception occurred. It is typically used for cleanup tasks.

### Q2. Why use `raise ... from e`?

The `raise ... from e` syntax is used for **exception chaining**. It raises a new exception while preserving the original exception as its cause. This makes debugging easier because the traceback shows both the custom `ConfigError` and the original exception (such as `FileNotFoundError` or `JSONDecodeError`).


###Q.13
## Q1. What problem do virtual environments solve?

Virtual environments isolate a project's Python interpreter and installed packages from other projects. This prevents dependency and version conflicts, allowing different projects to use different versions of the same package without affecting each other.

### Q2. Difference between pip freeze and a handwritten requirements.txt?

pip freeze lists every installed package in the current environment, including indirect dependencies.
A handwritten requirements.txt usually includes only the packages that the project directly depends on, making it cleaner and easier to maintain.


### Q.14
## Q1. What does `if __name__ == "__main__":` actually check?

Every Python module has a built-in variable called `__name__`. When a file is run directly, Python sets `__name__` to `"__main__"`. When the file is imported as a module, `__name__` is set to the module's name instead. Therefore, code inside `if __name__ == "__main__":` runs only when the file is executed directly, not when it is imported.

### 5-line demo

```python
def greet():
    print("Hello!")

if __name__ == "__main__":
    greet()

##Q2. Q2. Why is modifying sys.path a code smell?
Modifying sys.path manually makes imports depend on runtime path changes, which reduces portability and makes projects harder to maintain. A better approach is to organize code into packages using __init__.py, allowing Python to resolve imports naturally through the package structure.

# Bad
import sys
sys.path.append("src")
import helper

# Better
from app import helper