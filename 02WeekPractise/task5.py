year,month,day = input("Please enter date YYYY-MM-DD").split()

a = int(year)
b = int(month)
c = int(day)

result = (0<c<=30 and (b==4 or b==6 or b==9 or b==11))\
        or (0<c<32 and (b==1 or b==3 or b==5 or b==7 or b==10 or b==12))\
        or (0<c<=28 and b==2)\
        or (0<c<=29 and ((a%4==0 and a%100!=0) or (a%400==0)))


print("Date valid: " + str(result))

