import os
from methods import *

base_path = "D:\\Users\\jange\\Downloads"
dir_list = os.listdir(base_path)

for file in dir_list:
    path = os.path.join(base_path, file)
    if os.path.isfile(path):
        moveFile(file, base_path)

