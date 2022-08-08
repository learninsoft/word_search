import os
import sys
import traceback
import glob

import PyPDF2
from tqdm import tqdm

from database import configure_database, execute_query
from helper import process_word


def get_txt_content(filepath):
    with open(filepath, 'r') as f:
        data = f.read()
    return data


def get_pdf_content(filepath):
    data = ""
    with open(filepath, 'rb') as fhandle:
        pdfReader = PyPDF2.PdfFileReader(fhandle)
        count = pdfReader.numPages
        output = ""
        # Loop to read all the pages in PDF
        for i in range(min(5, count)):
            page = pdfReader.getPage(i)
            output += page.extractText()
        data = output
    return data


def get_doc_content(filepath):
    # TODO: extract the text from docx file
    return ""


def get_file_content(filepath):
    data_return = []
    try:
        data = ""
        if os.path.splitext(filepath)[1].lower() in ('.txt', ):
            data = get_txt_content(filepath)
        elif os.path.splitext(filepath)[1].lower() in ('.pdf', ):
            data = get_pdf_content(filepath)
        elif os.path.splitext(filepath)[1].lower() in ('.docx', 'doc', ):
            get_doc_content(filepath)
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

    file_types = []
    if sub_folders:
        file_types.append(glob.iglob(os.path.join(folder_path, "**\\*.[Tt][xX][Tt]"), recursive=True))
        file_types.append(glob.iglob(os.path.join(folder_path, "**\\*.[Pp][Dd][Ff]"), recursive=True))
        file_types.append(glob.iglob(os.path.join(folder_path, "**\\*.[Dd][Oo][Cc][Xx]"), recursive=True))
    else:
        file_types.append(glob.iglob(os.path.join(folder_path, "*.[Tt][xX][Tt]")))
        file_types.append(glob.iglob(os.path.join(folder_path, "*.[Pp][Dd][Ff]")))
        file_types.append(glob.iglob(os.path.join(folder_path, "*.[Pp][Dd][Ff]")))
        file_types.append(glob.iglob(os.path.join(folder_path, "*.[Dd][Oo][Cc][Xx]")))

    for files_generator in file_types:
        for filepath in files_generator:
            words_in_file = get_file_content(filepath)
            print(filepath, len(words_in_file))
            for word in tqdm(words_in_file):
                word = process_word(word)
                execute_query(filepath, word)


if __name__ == "__main__":
    try:
        generate_indexes(folder_path="D:\\", sub_folders=False)
    except KeyboardInterrupt:
        sys.exit(0)
