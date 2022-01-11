from random import randint
high = int(input('the maximum number?'))
low = int(input('the minumim number?'))
def Inc():
    return randint(low, high)

val = input("Enter your value: ")
print(val)
print("Your Value. ^")

print(Inc())
print("Computer Generated Value ^")

if (Inc())==(val):
    print("Equal")
else:
    print("Not equal")

