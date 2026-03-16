'''
1. Pascals Triangle
n = 5
Output: 
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''
n = int(input())
arr = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(i+1):
        if j == 0 or j == i:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        
        print(arr[i][j], end=" ")
    print()