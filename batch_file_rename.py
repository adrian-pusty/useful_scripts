# Replace unwanted string in all files in specific directory with another string
import os
import sys


def batch_file_rename(path, str_to_be_replaced, replace_with):
    files = os.listdir(path)
    for index, filename in enumerate(files):
        os.rename(os.path.join(path, filename), os.path.join(path, filename.replace(str_to_be_replaced, replace_with)))


try:
    batch_file_rename(sys.argv[1], sys.argv[2], sys.argv[3])
except:
    print('Wrong arguments, try again. Usage: ')
    print('python batch_renamer.py /path/to/directory/with/files str_to_be_replaced replace_with')
