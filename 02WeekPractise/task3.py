num1 = int(input("Please enter first even integers"))
num2 = int(input("Please enter second even integer"))


result = num1%2==0 and num2%2==0
print(("Both results are even: ") + str(result))

result = num1%2==0 or num2%2==0
print(("At least one number is even :") + str(result))
