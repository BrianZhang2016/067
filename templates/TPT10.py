
ageOne = 21
ageTwo = 16

print(ageOne,ageTwo)

def swapAge (ageOne, ageTwo):
    storAge = ageOne
    ageOne = ageTwo
    ageTwo = storAge
    return ageOne, ageTwo

thing1,thing2 = swapAge(ageOne, ageTwo)

print(thing1,thing2)

matrix = [(1,2,3),(4,5,6),(7,8,9)]
for x in matrix:
    for y in x:
        print(y, end = " ")
    print()