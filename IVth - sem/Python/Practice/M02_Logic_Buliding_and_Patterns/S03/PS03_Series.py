'''
Arithmetic Series:
Input: 1 2 
Output: 1 3 5 7 9 11 13 15 17 19
'''
# a, d = map(int, input().split())

# for i in range(10):
#     print(a + i * d, end=" ")

'''
Geometric Series:
Input: 1 2 
Output: 1 2 4 8 16 32 64 128 256 512
'''
# a, r = map(int, input().split())

# for i in range(10):
#     print(a * (r ** i), end=" ")

'''
Fibonacci Series:
Input: 5
Output: 0 1 1 2 3 
'''

# n = int(input())

# a, b = 0, 1

# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

'''
Fibonacci Series in a list:
Input: 5
Output: [0, 1, 1, 2, 3]
'''

# n = int(input())
# li = [0, 1]
# for i in range(2, n):
#     li.append(li[i - 1] + li[i - 2])
# print(li)

'''
Factorial of a number: 
Input: 5
Output: 120
'''

n = int(input())
if n < 0:
    print("Error")
elif n == 1 or n == 0:
    print(1)
else:
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print(fact)
