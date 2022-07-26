import sqlite3
import sys
import traceback

from helper import process
from configuration import Settings


def search_word(word_to_search, same_case=True):
    select_result = ()
    mydb, mycursor = None, None
    try:
        mydb = sqlite3.connect(Settings.DBNAME)
        mycursor = mydb.cursor()
        word = process(word_to_search)
        if same_case:
            select_query = f"select * from files_word where word = '{word}'"
        else:
            select_query = f"select * from files_word where lower(word) = '{word.lower()}'"
        mycursor.execute(select_query)
        select_result = mycursor.fetchall()
    except:
        traceback.print_exc()
        select_result = ()
    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()
        return select_result


if __name__ == "__main__":
    try:
        print(search_word(word_to_search="System", same_case=True))
    except KeyboardInterrupt:
        sys.exit(0)
