word_name = ["Paras", "Krishna", "Varsha", "Dwarkesh", "Wizzard"]
 
longest_length = 0
longest_word = ""

for word in word_name:
    length = 0
    
    for alpha in word:
        length= length + 1
    
    if length > longest_length:
        longest_length = length
        longest_word = word

print("Longest Length = ",longest_length)
print("longest word = ",longest_word)