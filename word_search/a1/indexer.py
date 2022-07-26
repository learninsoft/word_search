import os
import sys
import traceback
import glob
from tqdm import tqdm

from database import configure_database, execute_query
from helper import process

def get_file_content(filepath):
    data_return = []
    try:
        with open(filepath, 'r') as f:
            data = f.read()
        data_return = data.split()
    except:
        traceback.print_exc()
        data_return = []
    finally:
        return data_return


def generate_indexes(folder_path="", sub_folders=True):
    configure_database()

    if not os.path.exists(folder_path):
        return None

    if sub_folders:
        files_generator = glob.iglob(os.path.join(folder_path, "**\\*.[Tt][xX][Tt]"), recursive=True)
    else:
        files_generator = glob.iglob(os.path.join(folder_path, "*.[Tt][xX][Tt]"))

    for filepath in files_generator:
        words_in_file = get_file_content(filepath)
        print(filepath, len(words_in_file))
        for word in tqdm(words_in_file):
            word = process(word)
            execute_query(filepath, word)


if __name__ == "__main__":
    try:
        generate_indexes(folder_path="E:\\", sub_folders=True)
    except KeyboardInterrupt:
        sys.exit(0)
