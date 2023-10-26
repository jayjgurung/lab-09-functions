def factorial(n):
    fact = 1
    for i in range(1,n+1,1):
        fact = fact * i
    return fact

userInput = input("Enter a number to calculate factorial..\n")
userNum = int(userInput)
print(factorial(userNum))