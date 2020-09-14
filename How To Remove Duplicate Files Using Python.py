from tkinter import Tk
from tkinter.filedialog import askdirectory
import os, hashlib
from pathlib import Path


Tk().withdraw()  # to hide the small tk window
path = askdirectory(title='Select Folder')  # shows dialog box and return the path

files_list = os.listdir(path)  # take all the filename as a list

unique = dict()  # making a dictionary named unique

for file in os.listdir(path):   # looping over the file list

    file_name = Path(os.path.join(path, file))  # make a absolute file name using os.path.join function
    if file_name.is_file():  # checking the the the item is file or not

        # A tool for creating an MD5 hash from a string
        # The Python hashlib module is an interface for hashing messages easily. This contains numerous methods which
        # will handle hashing any raw message in an encrypted format
        # hexdigest() : Returns the encoded data in hexadecimal format
        fileHash = hashlib.md5(open(file_name, 'rb').read()).hexdigest()


        if fileHash not in unique:
            unique[fileHash] = file_name

        else:
            # print(file_name)
            os.remove(file_name)
        print(f"Successfully deleted {file_name}")
    else:
        print("Path not exits")


