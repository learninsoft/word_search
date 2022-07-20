word_to_search = 'g<zl'

import os

files_dir = "text_files"

for file in os.listdir(files_dir):

    filename = "text_files/" + file

    with open(filename, "r") as infile:
        data = infile.read()

    list_of_words = data.split()

    if word_to_search in list_of_words:
        print("filename: ", filename)


# Indexing

# Index.


# To create the index.

# whenever the user enters the word, just look into the index.

# word1, filename1
# word1, filename1
# word1, filename1

# word1, filename1
# word2, filename1
# word_n, filename1
# word1, filename2
# word2, filename2

# y8n7q, text_files/0.txt
# l)7w(s<5F3, text_files/0.txt
# C/8H, text_files/0.txt
# 8y<>u, text_files/1.txt
#

# local database.

# mysql.

# sqlite3

# android applications.
# sqlite3

import sqlite3
mydb = sqlite3.connect("barium_search.db")

cursor_obj = mydb.cursor()

create_table = """
create table if not exists files_words
(filename varchar(255), 
word varchar(255),

);
"""

cursor_obj.execute(create_table)

cursor_obj.close()
mydb.close()

