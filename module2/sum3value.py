num1=int(input("enter first number---"))
num2=int(input("enter second number---"))
num3=int(input("enter third number---"))


sum=0

sum=num1+num2+num3

print("sum is --",sum)

if num1==num2 or num2==num3 or num1==num3:
    print("sum is zero")
else:
    print("not zero")    