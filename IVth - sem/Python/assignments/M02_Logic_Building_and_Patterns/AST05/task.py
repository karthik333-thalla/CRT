
def number_triangle(n: int) -> str:
    """
    Returns a number triangle pattern for given n.
    
    Example for n=4:
    1
    12
    123
    1234
    """
    result = []
    for i in range(1, n + 1):
        row = ''.join(str(j) for j in range(1, i + 1))
        result.append(row)
    return '\n'.join(result)


if __name__ == "__main__":
    n = int(input())
    print(number_triangle(n))