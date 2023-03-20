
for number in range (1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# 2 solution:
# for number in range (1,101):
# printnumber = True
# if i % 3 == 0:
#     print("Fizz", end="")
#     printmuber = False

# if i % 5 == 0:
#     print("Buzz", end="")
#     printnumber = False

# if printumber:
#     print(i)
# else: #go to the next line
#     print()


