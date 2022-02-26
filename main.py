import os, shutil
from pathlib import Path
from exts import extensions


path = "D:\\Users\\jange\\Desktop\\testing"
dir_list = os.listdir(path)

    
def move(file):
    split = os.path.splitext(file)
    file_extension = split[1]

    for key in extensions:
        if file_extension in extensions[key]:
            shutil.move(f"{path}\\{file}", f"{path}\\{key}")

for file in dir_list:
    move(file)

