import os, shutil
from exts import extensions

def isInExt(file_extension):
    for key in extensions:
        if file_extension in extensions[key]:
            return True
    return False

def renameFile(new_path, file, file_name, file_extension):
    i = 1
    temp = os.path.join(new_path,file)
    while os.path.exists(temp):
        new_name = f"{file_name}({i}){file_extension}"
        temp = os.path.join(new_path,new_name)
        i+=1
    return new_name

def moveFile(file, base_path):
    split = os.path.splitext(file)
    file_name = split[0]
    file_extension = split[1]
    from_path = os.path.join(base_path, file)
    
    if isInExt(file_extension):
        for key in extensions:
            if file_extension in extensions[key]:
                from_path = os.path.join(base_path, file)
                new_path = os.path.join(base_path, key)
                new_name = file

                if os.path.exists(os.path.join(new_path, file)):
                    new_name = renameFile(new_path, file, file_name, file_extension)

                shutil.move(from_path, os.path.join(new_path, new_name))
    else:
        new_path = os.path.join(base_path, f"Others/")
        new_name = file
        if os.path.exists(os.path.join(new_path, file)):
            new_name = renameFile(new_path, file, file_name, file_extension)

        shutil.move(from_path, os.path.join(new_path, new_name))