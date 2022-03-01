
print("Swap")
ageOne = 21
ageTwo = 16

print(ageOne,ageTwo)

def swapAge (ageOne, ageTwo):
    storAge = ageOne
    ageOne = ageTwo
    ageTwo = storAge
    return ageOne, ageTwo

age1,age2 = swapAge(ageOne, ageTwo)

print(age1,age2)

print("-----")

print("Matrix")
#matrix
matrix = [(1,2,3),(4,5,6),(7,8,9), (" ",0," ")]
for x in matrix:
    for y in x:
        print(y, end = " ")
    print()