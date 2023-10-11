# Function to swap the first two characters of two strings and combine them with a space
def swap_and_combine_strings(str1, str2):
    # Check if both strings have at least 2 characters
    if len(str1) < 2 or len(str2) < 2:
        print ("Both strings should have at least 2 characters.")
    
    # Swap the first two characters of each string
    swapped_str1 = str2[:2] + str1[2:]
    swapped_str2 = str1[:2] + str2[2:]
    
    # Combine the swapped strings with a space in between
    result = swapped_str1 + " " + swapped_str2
    
    return result

# Input two strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Call the function to swap and combine the strings
result_string = swap_and_combine_strings(string1, string2)

# Display the result
print("Result:", result_string)
