from functools import lru_cache


@lru_cache(maxsize=None)
def unique_sorted_digits(digits_left: int, max_digit_placed: int) -> int:
    if digits_left == 0:
        return 1
    return sum([unique_sorted_digits(digits_left - 1, new_max_digit) for new_max_digit in range(max_digit_placed, 10)])


@lru_cache(maxsize=None)
def sorted_digits_sum(digits_left: int, max_digit_placed: int) -> int:
    if digits_left == 0:
        return 0
    return sum([sorted_digits_sum(digits_left - 1, new_max_digit) for new_max_digit in range(max_digit_placed, 10)])


if __name__ == '__main__':
    print(unique_sorted_digits(36, 0))
