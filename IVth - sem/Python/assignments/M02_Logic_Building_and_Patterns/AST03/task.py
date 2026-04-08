# task.py

def sum_of_digits(n: int) -> int:
    """
    Returns the sum of digits of a number.
    
    Example:
    123 -> 6
    """
    # Handle negative numbers
    n = abs(n)

    # Convert to string and sum digits
    return sum(int(digit) for digit in str(n))


if __name__ == "__main__":
    n = int(input())
    print(sum_of_digits(n))