def count_words(sentence):
    # Convert the sentence to lowercase
    sentence = sentence.lower()

    # Split the sentence into words
    words = sentence.split()

    # Create a dictionary to store the word counts
    word_counts = {}

    # Iterate over each word in the words list
    for word in words:
        # If the word is already in the dictionary, increment its count
        if word in word_counts:
            word_counts[word] += 1
        # Otherwise, add the word to the dictionary with a count of 1
        else:
            word_counts[word] = 1

    # Return the dictionary of word counts
    return word_counts

# Test the function with a sample sentence
sentence = "This is a sample sentence. This sentence is a sample for the function."
print(count_words(sentence))