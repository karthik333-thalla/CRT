# task.py

def right_triangle(n: int) -> str:
    """
    Returns a right triangle star pattern for given n.
    
    Example for n=5:
    *
    **
    ***
    ****
    *****
    """
    result = []
    for i in range(1, n + 1):
        row = '*' * i
        result.append(row)
    return '\n'.join(result)


if __name__ == "__main__":
    n = int(input())
    print(right_triangle(n))
