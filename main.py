from functools import lru_cache
from tools import measure


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
