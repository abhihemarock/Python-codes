a=int(input())
if(a%4==0):
    print("it is a leap year")
elif(a%100==0 or a%400==0):
    print("it is a leap year") 
else:
    print("|it is not a leap year")
    