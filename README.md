# Fibonacci Sequence Optimization with `lru_cache`

This repository explores the use of Python's lru_cache decorator to optimize the calculation of Fibonacci numbers. Additionally, a custom decorator is employed to measure function execution time.

The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, starting from 0 and 1. The naive recursive approach to calculating a Fibonacci number has an exponential time complexity of $O(2^n)$.
To enhance performance, this repository uses memoization via Python's built-in lru_cache decorator. Memoization is a technique that stores the results of function calls and returns the precomputed result when the same inputs occur again. 

**This improves the time complexity from $O(2^n)$ to $O(n)$ for initial calculations and $O(1)$ for subsequent lookups of already calculated values.**


## Table of Contents

- [Prerequisites](#Prerequisites)
- [Installation](#Installation)
- [Usage](#Usage)
- [Understanding the Code](#understanding-the-code)
- [Least Recently Used (LRU) Cache](#understanding-the-code)
- [Big-O Complexity](#Big-O-Complexity)
- [Problems using lru_cache on instance methods](#Problems-using-lru_cache-on-instance-methods)

## Prerequisites
- Python 3.8
- pip

## Installation
1. Clone this repository:
    ```
    git clone https://github.com/phgas/lru_cache.git
    ```
2. Navigate into the project directory
    ```
    cd lru_cache
    ```

## Usage
Run the `main.py` file in the Python environment.
```bash
python main.py
```

## Understanding the Code
The `main.py` file contains the Fibonacci function decorated with `lru_cache`, and a `main()` function decorated with a custom `measure` function to log the execution time.

Here's the code snippet:
```python
from functools import lru_cache
from tools import measure  # A custom decorator to measure time

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

@measure
def main():
    result: int = fib(400)
    print(result)

if __name__ == "__main__":
    main()
```

- `@lru_cache(maxsize=None)`: Caches the result of each unique function call.
- `@measure`: Measures the time taken by the function to execute.

## Least Recently Used (LRU) Cache
A Least Recently Used (LRU) Cache organizes items in order of use, allowing to quickly identify which item hasn't been used for the longest amount of time.
When adding a new item to a full cache, the least recently used item is removed. If an existing item is accessed, it becomes the most recently used item.

In our case, `maxsize` specifies the maximum size that the `lru_cache()` can hold. 
Once this size is reached, the least recently used item is evicted to make room for a new one.

For a more in-depth understanding of the LRU Cache, you can visit: [Interview Cake's LRU Cache Concept](https://www.interviewcake.com/concept/java/lru-cache)

## Big-O Complexity
<p align="center">
  <img src="https://github.com/phgas/lru_cache/assets/89270047/173686ae-7161-4265-8c7a-64de007badb4">
</p>
<p align="center">Big-O Complexity Chart: http://bigocheatsheet.com/</p>

### Without `lru_cache`
The naive recursive algorithm to calculate fib(n) has a time complexity of $O(2^n)$ due to redundant calculations.
### With `lru_cache`
Using lru_cache, the algorithm's time complexity is reduced to $O(n)$ as each unique Fibonacci number is computed only once and then stored for future use in the cache.


## Problems using lru_cache on instance methods
### Memory Leaks: 
When you use lru_cache on instance methods, the cache keeps references to the object instances. This means the instances can't be garbage collected even if they're no longer in use, leading to memory leaks.
### Unexpected Caching Behavior: 
Each instance of the class has its own set of cached results. Therefore, the cache doesn't work as expected across different instances, leading to inefficiencies. 

If you are interested in possible solutions or want to dive deeper take a look here: [anthonywritescode](https://www.youtube.com/watch?v=sVjtp6tGo0g) 
