def count_substring_occurrences(main_string, substring):
  count = main_string.count(substring)
  return count

# Input the main string and the substring to search for
main_string = input("Enter the main string: ")
substring = input("Enter the substring to count: ")

result = count_substring_occurrences(main_string, substring)

print(f"The substring '{substring}' appears {result} times in the main string.")
