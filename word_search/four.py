
import os
import sqlite3
mydb = sqlite3.connect("barium_search.db")
cursor_obj = mydb.cursor()


files_dir = "text_files"

for file in os.listdir(files_dir):

    filename = "text_files/" + file

    with open(filename, "r") as infile:
        data = infile.read()

    list_of_words = data.split()
    for word in list_of_words:
        word = word.replace("'", " ")
        insert_query = f"""
        INSERT INTO files_words(filename, word) values ( '{filename}','{word}');
        """
        try:
            cursor_obj.execute(insert_query)
        except(sqlite3.IntegrityError):
            print()
    mydb.commit()

cursor_obj.close()
mydb.close()
