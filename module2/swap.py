a=50
b=60

temp=a
b=temp
a=b
b=a
 
print(f"a with temp {a} b with temp is {b}") 

a,b=b,a

print(f"a without temp {a} b without temp {b}")