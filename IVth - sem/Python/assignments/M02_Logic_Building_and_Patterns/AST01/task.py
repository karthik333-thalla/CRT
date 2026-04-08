def count_digits(n: int) -> int:
    """
    Returns the number of digits in a number.
    """
    # Handle negative numbers
    n = abs(n)

    # Special case: 0 has 1 digit
    if n == 0:
        return 1

    # Convert to string and count length
    return len(str(n))


if __name__ == "__main__":
    n = int(input())
    print(count_digits(n))