import os

directory_name = "data_store"
current_directory = os.getcwd()

os.chdir(current_directory + "/" + directory_name)
files_in_dir = os.listdir()


#print(files_in_dir)
