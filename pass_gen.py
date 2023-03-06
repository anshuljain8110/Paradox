import random
#defined combinations
lowers = 'qwertyuiopasdfghjklzxcvbnm'
uppers = 'QWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '1234567890'
symbols = '!@#$%^&*_'
combination = lowers + uppers + numbers + symbols

k=1
while k==1:
    #enter the length of password required
    length = input("Enter the length of password required (between 8 and 24): ")
    length_int= int(length)
    if 7<length_int<25:

        #generate the password
        password = ''.join(random.sample(combination, length_int))

        #here the password you got!
        print("Password:", password)
    else:   
        print("The length of password should be between 8 and 24")

    print("Enter 0 to exit or 1 to generate a new password")

    # For restarting or exiting 
    k=int(input())
    if k==0:
        break
    elif k!=1:
        print("Enter either 0 or 1")
        k=int(input())