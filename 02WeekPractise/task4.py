year = int(input("Check if year is leap. Please enter year"))

result = (year%4==0 and year%100!=0) or (year%400==0)
print("These year are leap year: "+str(result))