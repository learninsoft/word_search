import sqlite3
mydb = sqlite3.connect("barium_search.db")
cursor_obj = mydb.cursor()

create_table = """
create table if not exists files_words
(filename varchar(255), 
word varchar(255),
primary key (filename, word)
);
"""

cursor_obj.execute(create_table)
cursor_obj.close()
mydb.close()
