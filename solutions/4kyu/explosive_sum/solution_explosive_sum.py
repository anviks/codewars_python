"""https://www.codewars.com/kata/52ec24228a515e620b0005ef"""


def memoize(func):
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return wrapper


@memoize
def exp_sum(n: int) -> int:
    """
    Ten times faster than exp_sum_2, but raises an error for n > 3000.
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n <= 3:
        return n
    counter = 1
    counter_odd = 1
    temp_n = n
    result = 0
    while temp_n > 3:
        temp_n -= counter_odd
        result += exp_sum(temp_n)
        temp_n -= counter
        result += exp_sum(temp_n)
        counter += 1
        counter_odd += 2

        temp_n -= counter_odd
        result -= exp_sum(temp_n)
        temp_n -= counter
        result -= exp_sum(temp_n)
        counter += 1
        counter_odd += 2

    return result


def exp_sum_2(n: int) -> int:
    """
    Ten times slower than exp_sum, but doesn't raise an error for n > 3000. Generated by ChatGPT.
    """
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]

    return dp[n]