import os, shutil
from pkgutil import read_code
from pathlib import Path
from exts import extensions

base_path = "D:\\Users\\jange\\Desktop\\testing"
dir_list = os.listdir(base_path)

def moveFile(file):
    split = os.path.splitext(file)
    file_name = split[0]
    file_extension = split[1]

    for key in extensions:
        if file_extension in extensions[key]:
            from_path = os.path.join(base_path, file)
            new_path = os.path.join(base_path, key)
            new_name = file

            if os.path.exists(os.path.join(new_path, file)):
                i = 1
                temp = os.path.join(new_path,file)
                while os.path.exists(temp):
                    new_name = f"{file}({i}){file_extension}"
                    temp = os.path.join(new_path,new_name)
                    i+=1

            shutil.move(from_path, os.path.join(new_path, new_name))

for file in dir_list:
    moveFile(file)

