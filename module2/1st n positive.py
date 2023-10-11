def sum_of_first_n_integers(n):
    if n <= 0:
        return "Please enter a positive integer."
    
    total = 0
    for i in range(1, n + 1):
        total += i
    
    return total

# Input the value of n
n = int(input("Enter a positive integer n: "))

result = sum_of_first_n_integers(n)

if isinstance(result, int):
    print(f"The sum of the first {n} positive integers is: {result}")
else:
    print(result)
    
    
    
