a=int(input("Enter First Integer :- "))
b=int(input("Enter Second Integer :- "))
c=int(input("Enter Third Integer :- "))

if a == b or b == c or c == a:
    print("Two Integers are equal")
    sum = 0
else:
    sum= a + b + c
    
#print("Sum = {} + {} + {} = ".format(a,b,c,sum))
print(f"sum is {a}+{b}+{c}={sum}")