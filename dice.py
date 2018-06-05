import random

def dieroller(y):
        print("you have rolled a %s" % random.randint(1,6), end ="")
        for item in range(0, int(y)-2):
            print(", %s" %  random.randint(1,6), end ="")
        print(', and a %s' % random.randint(1,6))
            
            
print ('Welcome to the python dice simulator!')

user_input = input('Enter the number of dice you would like to roll as an integer and hit ENTER: ')

dieroller(user_input)

