def are_values_equal_or_sum_difference_5(a, b):
    if a == b or abs(a - b) == 5 or a + b == 5:
        return True
    else:
        return False

# Test cases
value1 = int(input("Enter the first integer: "))
value2 = int(input("Enter the second integer: "))

result = are_values_equal_or_sum_difference_5(value1, value2)

if result:
    print("True")
else:
    print("False")
