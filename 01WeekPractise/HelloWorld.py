age = input("Please enter your age")
licence = input("Do you have licence? Yes/No")

result = int(age) >= 18 and licence == "Yes" or licence=="yes"
print(("You are able to drive") + str(result))

