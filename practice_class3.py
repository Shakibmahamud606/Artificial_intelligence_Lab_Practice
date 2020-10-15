var = []
for i in range(5):
    var.append(int(input("Enter a value: ")))

print(var)
# backword calling  from list
print(var[-1])
# 0 to before 3  value will  be  printed
print(var[0:3])
# from 1 position to last will be printed
print(var[1:])
# printing all number before position 2
print(var[:2])
# from last  to brfore -3 position
print(var[-3:-1])
# lenth of the list
print(len(var))
# inserting  a new valo to a position
var.insert(2, 9606)
print(var)
# poping from list
var.pop()
print(var)


# poping from list position wise
var.pop(0)
print(var)

# adding to a new list even number
new_var = []
for n in var:
    if n % 2 == 0:
        new_var.append(n)
print(new_var)

# in one line same work as before
new_var_two = [n for n in var if n % 2 == 0]
print(new_var_two)

# reverse funtion
new_var_two.reverse()
print(new_var_two)

# sorting
new_var_two.sort()
print(new_var_two)

#  coverting to tuple
sk_t_var2 = tuple(new_var_two)
print(sk_t_var2)
