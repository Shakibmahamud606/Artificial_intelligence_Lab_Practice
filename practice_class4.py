# string
name = 'My Bnagladesh'
# lenth of the  funtion
print(len(name))
# Spliting into Words
print(name.split())
# printing  as  index position
print(name[2:5])

# funtions
# how dose funtion Works all in one funtion


def addNumber(x, y, z=2):
    sum = x+y+z
    print("Sum = {} + {} + {} = {}".format(x, y, z, sum))
    return sum


addtion = addNumber(5, 6, 7)
print(addtion)


# for default value
# python  gives a extra thing adding a defult value


def addNumbers(x, y, z=2):
    sum = x+y+z
    print("Sum = {} + {} + {} = {}".format(x, y, z, sum))
    return sum


addNumbers(5, 6)
