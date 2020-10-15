var = []
n = int(input())
for i in range(n):
    var.append(int(input()))
list1 = []
print("List 1 = ", end='')
for x in var:
    if x % 2 == 0:
        list1.append(-x*2+x)
    else:
        list1.append(0)
list1
list2 = [x for x in var if x < 0]
print("List 2 = ", end='')
print(list2)
tuple_var = tuple(list2)
print("Tuple = ", end='')
# type(tuple_var)
print(tuple_var)
