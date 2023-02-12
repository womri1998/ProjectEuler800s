import math
from math import log
from typing import Generator


Pair = tuple[int, int]


def max_prime(max_value: float) -> int:
    i = 3
    while compare((2, i), max_value):
        i += 1000
    return i


def gen_primes(n) -> list[int]:
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(math.ceil(n ** 0.5)):
        if primes[i]:
            for j in range(2 * i, n, i):
                primes[j] = False
    return [i for i in range(n) if primes[i]]


def pair_log_value(p: int, q: int) -> float:
    return p * log(q) + q * log(p)


def compare(prime_pair: Pair, max_value: float) -> bool:
    return pair_log_value(*prime_pair) < max_value


def main(max_generator: int):
    count = 0
    max_value = max_generator * log(max_generator)
    limit = max_prime(max_value)
    primes = gen_primes(limit)
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if compare((primes[i], primes[j]), max_value):
                count += 1
            else:
                if i % 100 == 0:
                    print(primes[i])
                break
    print(count)


if __name__ == "__main__":
    main(800)
    main(800800)
