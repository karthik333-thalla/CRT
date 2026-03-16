# -------------------------------------------#COUNTING NUMBERS---------------------------------------------------------------
'''
sample input : 1234
sample output : 4

sample input : 12236
sample output : 5
'''

# n = int(input("Enter a number: "))
# count = 0
# while n > 0:
#     count += 1
#     n = n // 10
# print("Number of digits:", count)

# -------------------------------------------#SUM OF DIGITS---------------------------------------------------------------

'''
sample input : 1234
sample output : 10

sample input : 12236
sample output : 14
'''

# n = int(input("Enter a number: "))
# summ = 0
# while n > 0:
#     digit = n%10
#     summ += digit
#     n = n //10
# print("Sum of digits:", summ)

# -------------------------------------------# PRINT ONLY EVEN DIGITS---------------------------------------------------------------

'''
sample input : 1234
sample output : 4 2 

sample input : 12236
sample output : 6 2 2
'''
# def reverse(num):
#     rev = 0
#     while num > 0:
#         rev = (rev * 10) + (num % 10)
#         num = num // 10
#     return rev

# n = reverse(int(input("Enter a number: ")))
# while n > 0:
#     digit = n % 10
#     if(digit%2 == 0):
#         print(digit, end = " ")
#     n = n // 10
        

# ------------------------------------------# REVERSING A NUMBER---------------------------------------------------------------

'''
sample input : 1234
sample output : 4321

sample input : 12236
sample output : 63221
'''
# n = int(input("Enter a number: "))
# rev = 0

# while n > 0:
#     rev = rev * 10 + (n % 10)
#     n //= 10

# print(rev)

# ------------------------------------------# PALINDROME CHECKING---------------------------------------------------------------
def reverse(num):
    rev = 0
    while num > 0:
        rev = (rev * 10) + (num % 10)
        num = num // 10
    return rev
n = int(input("Enter a number: "))
temp = reverse(n)
if temp == n: 
    print(True)
else:
    print(False)
