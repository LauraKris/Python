number1 = float(input("Enter 1st number\n"))
number2 = float(input("Enter 2nd number\n"))

while True:
    operation = input("Enter operation (*,/,+,- or %)")
    if (operation == "*"):
        result = number1 * number2
    elif(operation == "/"):
        result = number1 / number2
    elif(operation == "+"):
        result = number1 + number2
    elif(operation == "-"):
        result = number1 - number2
    elif(operation == "%"):
        result = number1 % number2
    else:
        print("operation is not correct")
        continue
    print("Result is" + str(result))
    break

#while butinai naudojamas su break, kad butu pabaigtas veiksmas