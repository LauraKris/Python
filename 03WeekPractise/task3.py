number = int(input("Enter number in order to get a factorial of it\n"))
for i in range (1,number):
    if(number % i == 0):
        print(i)

print(number)


#2 solution
number = int(input("Enter number in order to get a factorial of it\n"))
if number < 0:
    print(-1)
    for i in range (-2,number,-1):
        print(i)
    print(number)
elif number > 0:
    print(1)
    for i in range (2, number):
        if(number % i == 0):
            print(i)
    print(number)
else:#0
    print("All the numbers")
