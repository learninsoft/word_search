import sqlite3
import traceback

from configuration import Settings


def configure_database():
    """
    This function creates sqlite database, and one table.
    :return: status dictionary of message.
    """
    mydb, mycursor = None, None
    status = {"message": False}
    try:
        mydb = sqlite3.connect(Settings.DBNAME)
        mycursor = mydb.cursor()
        create_table_query = ("Create table if not exists files_word("
                              "filepath varchar(255), "
                              "word varchar(255), "
                              "word_count int default 1, "
                              "PRIMARY KEY(filepath, word))")
        mycursor.execute(create_table_query)
        mydb.commit()

        status["message"] = "Database and table created"
    except:
        traceback.print_exc()
        status['message'] = "error"
    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()
    return status


def execute_query(filepath, word):
    mydb, mycursor = None, None
    status = {"message": False}
    try:
        mydb = sqlite3.connect(Settings.DBNAME)
        mycursor = mydb.cursor()
        insert_query = f"INSERT INTO files_word(filepath, word) values ('{filepath}', '{word}')"
        try:
            mycursor.execute(insert_query)
        except sqlite3.IntegrityError as err_msg:
            upd_query = f"Update files_word set word_count=word_count+1 where filepath = '{filepath}' and word = '{word}'"
            mycursor.execute(upd_query)
        mydb.commit()
        status["message"] = f"executed successfully for {filepath} and {word}"
    except:
        traceback.print_exc()
        status['message'] = "error"
    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()
    return status
