'''
1. Square Star Pattern

Input: n = 4
Output: 
* * * *
* * * *
* * * *
* * * *
'''
# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print("*", end = " ")
#     print()

'''
2. Right Angle Triangle Pattern
Input: n = 4
Output: 
* 
* * 
* * * 
* * * * 
'''

# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         p2rint("*", end = " ")
#     print()

'''
3. Inverted Right Angle Triangle Pattern
Input: n = 4
Output:
* * * *
* * *
* *
*
'''

n = int(input())

for i in range(-n, n + 1):
    for j in range(-n, n + 1):
        if i*i + j*j == n*n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

