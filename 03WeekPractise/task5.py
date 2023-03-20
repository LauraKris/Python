number = int(input("Enter number\n"))

prime = True
for i in range (2, number):
    if (number%1 == 0):
        prime = False

if number > 1 and prime:
    print("Number is prime")
else:
    print("Number is not prime")