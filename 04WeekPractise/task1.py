#1.Ask the user to enter the text and a letter. Count how many occurrences of the letter provided. 
#1.1 Based on the task 1, count the occurrences of each character in the text provided and display them in the output

# text = input("Enter text:\n")
# symbol = input ("Enter a symbol that you like to count:\n")

# count = 0
# for char in text:
#     if char == symbol:
#         count+= 1

# print("The letter {} appears {} times in the text.".format(symbol,count))

text = input("Enter text:\n")
symbol = input ("Enter a symbol that you like to count:\n")
match = search(symbol.text)

if match:
    count +=1

print("The letter {} appears {} times in the text.".format(symbol,match))