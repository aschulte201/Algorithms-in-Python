from functools import lru_cache


def f_basic(n: int):
    if n >= 2:
        return f_basic(n-1) + f_basic(n-2)
    return n


memo: dict = {0: 0, 1: 1}


def f_dict(n: int):
    if n not in memo:
        memo[n] = f_dict(n-1)+f_dict(n-2)
    return memo[n]


@lru_cache(maxsize=None)
def f_memo(n: int):
    if n >= 2:
        return f_memo(n-1) + f_memo(n-2)
    return n


def f_iter(n: int):
    if not n:
        return n
    last = 0
    next = 1
    for _ in range(1, n):
        last, next = next, last+next
    return next


def f_gen(n: int):
    yield 0
    if n > 0:
        yield 1
    last = 0
    next = 1
    for _ in range(1, n):
        last, next = next, last+next
        yield next


if __name__ == "__main__":
    print(f_memo(50))
    print(f_dict(50))
    print(f_iter(50))
    print(*f_gen(50))
