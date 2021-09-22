import os

directory_name = "data_store"
current_directory = os.getcwd()

os.chdir(current_directory + "/" + directory_name)
files_in_dir = os.listdir()

for file in files_in_dir:
    if not file.lower().endswith('.xlsx'):
        files_in_dir.remove(file)

#print(files_in_dir)
