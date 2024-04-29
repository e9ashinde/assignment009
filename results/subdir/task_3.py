import os
import shutil
pathdir=input("Enter the path here: ")
dest_dir=input("Enter the destination here: ")
files = os.listdir(pathdir)
for file in files:
    file_ext=os.path.splitext(file)[-1].lower()
    if file.endswith(".py"):
        src_path=os.path.join(pathdir,file)
        dest_path=os.path.join(dest_dir,file)
        shutil.move(src_path,dest_path)