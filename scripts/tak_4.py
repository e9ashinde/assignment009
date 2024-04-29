import os
def dir_size(path):
    size={}
    for path,dirs,files in os.walk(path):
        for f in files:
            fp=os.path.join(path,f)
            size[f]=os.path.getsize(fp)
    return size
print(dir_size("/home/sierra/repository/assignment009/results"))

# def sub_dir(path):
#     for dirpath, dirnames, _ in os.walk(path):
#         for dirname in dirnames:
#             subdir_path = os.path.join(dirpath, dirname)
#             size=dir_size(subdir_path)
#         print(f"Size of {subdir_path}: {size} bytes")

# if __name__ == "__main__":
#     user_input = input("Enter directory path: ")
#     sub_dir(user_input)
