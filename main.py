import os
import pandas as pd
import matplotlib.pyplot as plt


# get 3 charachers of string
def getCharacters(day_name):
    characters_count_needed = 3
    result = ""
    for index,char in enumerate(day_name):
        result = result + char
        if index == (characters_count_needed - 1):
            return result


# step 1
all_excel_files = []
def getFiles(maven_dir):
    #excel files are in directory named 'data_store' which is in the same directory
    os.chdir(maven_dir)
    excel_files_list = os.listdir()
    for item in excel_files_list:
        all_excel_files.append(item)


maven_dir = "data_store"
getFiles(maven_dir)

#step 2
# empty_times = [ ['Monday', '18 - 16'] , ['Monday', '12 - 10'], ... ]
empty_times = []
def findEmptyCells(file_name):
    current_directory = os.getcwd() # current dir NOW is maven_dir
    excel_file = current_directory +'\\' + file_name
    
    data = pd.read_excel(excel_file)
    data_arr = data.values
    
    all_rows_height= len(data_arr)
    row_width=len(data_arr[0])
    
    all_rows = []
    for i in range(0, all_rows_height):
        row=list(data_arr[i].flatten())
        for index,item in enumerate(row):
            #replace "nan" with ""
            if str(item)=="nan":
                row[index] = ""
        all_rows.append(row)
        
    for i, row in enumerate(all_rows):
        for j, item in enumerate(all_rows[i]):
            if item=='':
                time = all_rows[0][j]
                day = all_rows[i][row_width-1]
                day_short_name = getCharacters(day)
                empty_times.append( day_short_name +":"+time)
                

for file_name in all_excel_files:
    findEmptyCells(file_name)

#step 3
def showGraph(data_set):
    range = (0,10)
    bins = 3
    plt.hist(data_set,bins, range, histtype='bar', rwidth=1)
    plt.xlabel('')
    plt.ylabel('count')
    plt.title('empty times in week')
    plt.show()


showGraph(empty_times)
    


