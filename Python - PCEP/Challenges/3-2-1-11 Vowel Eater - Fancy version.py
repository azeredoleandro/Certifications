word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.

print("The world's most beautiful vowel eater!")
word_without_vowels = input("Type a word:")
user_word = word_without_vowels.upper()
final_word = ""

for letter in user_word:
    # Complete the body of the loop.
    if letter == "A":
        user_word = letter
    elif letter == "E":
        user_word = letter
    elif letter == "I":
        user_word = letter
    elif letter == "O":
        user_word = letter
    elif letter == "U":
        user_word = letter
    else:
        final_word = final_word + letter

word_without_vowels = final_word
    
# Print the word assigned to word_without_vowels.
  
if final_word == "":
    print("Empty result!")
else:
    print(final_word)
