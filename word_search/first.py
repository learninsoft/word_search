"""
1. Generate the data
2.
"""

import string
import random
import os

os.makedirs("text_files", exist_ok=True)

list_of_letters = list(string.ascii_letters+string.digits+string.punctuation+"\n")
# ` \

list_of_letters.remove('`')

list_of_letters.remove('\\')


print(list_of_letters)
for q in range(128):
    list_of_words = []

    for j in range(100):
        word = ""
        word_length = random.randint(2,10)
        for i in range(word_length):
            word += random.choice(list_of_letters)
        list_of_words.append(word)
        # print(f"word {j}: ===>   ", word)

    print(list_of_words)

    sentence = ""
    for i in list_of_words:
        sentence += i + " "

    print(sentence)

    # writing a sentence into a text file

    # filename = f"text_files/{q}.txt"
    # String formatting.
    filename = "text_files/"+str(q)+".txt"

    with open(filename, "w") as infile:
        infile.write(sentence)
