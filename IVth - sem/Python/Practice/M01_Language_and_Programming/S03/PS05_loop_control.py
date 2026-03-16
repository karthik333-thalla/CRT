for i in range(1, 11):
    if i == 5:
        continue
    print(i, end = " ")
else:
    print("Loop completed")

'''Password retry system (max 3 attempts)
If password is correct, print "Access granted"
Else ask for password 3 times 
Once attempts are exhausted, print "Access denied"
Original password is "admin123"
'''
user_name = input("Enter your username: ")
password = input("Enter your password: ")
ori_pass = "admin123"
attempts = 3
while attempts > 0:
    if password == ori_pass:
        print("Access granted")
        break
    else:
        attempts -= 1
        if attempts == 0:
            print("Access denied")
            break
        print(f"Incorrect password. You have {attempts} attempts left.")
        password = input("Re-enter your password: ")