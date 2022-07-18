"""
2. Read the data
"""
import os

files_dir = "text_files"

for file in os.listdir(files_dir):

    filename = "text_files/" + file

    with open(filename, "r") as infile:
        data = infile.read()

    print(data[:5], type(data))
