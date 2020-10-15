# taking input
number = int(input("Enter any number: "))
print(number)  # printing it

# Checking ODD or EVEN
if number < 0:
    print("Negetive")
elif number % 2 == 0 and number > 10:
    print("Even and greater then 10")
elif number % 2 == 0:
    print("The  Number Is "+str(number)+" EVEN")
else:
    print("The  Number Is "+str(number)+" ODD")
# taking input for loop
n = int(input("Enter a number where loop will stop:  "))
i = 0
# A simple loop
for i in range(0, n):
    print(i)
# printing to the Number user given
print('Printing to the Number user given')
while i <= n:
    print(i)
    i += 1
# incrementing by 2
print('incrementing by 2')
for i in range(0, n, 2):
    print(i)
