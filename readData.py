import pandas as pd
import os

# get 3 charachers of string
def getCharacters(day_name):
    characters_count_needed = 3
    result = ""
    for index,char in enumerate(day_name):
        result = result + char
        if index == (characters_count_needed - 1):
            return result


# MY_FILE_NAME.xlsx
data = pd.read_excel('test_file.xlsx')#read test_file.xlsx which is in the same directory
data_arr = data.values

#get count lists
all_rows_height= len(data_arr)
row_width=len(data_arr[0])

#replace 'nan' with "" and store them in all_rows array
all_rows = []
for i in range(0, all_rows_height):
    row=list(data_arr[i].flatten())
    for index,item in enumerate(row):
        if str(item)=="nan":
            row[index] = ""
    all_rows.append(row)


#searching for empty cells
empty_times = [] # empty_times = [ ['Monday', '18 - 16'] , ['Monday', '12 - 10'] ]
for i, row in enumerate(all_rows):
    for j, item in enumerate(all_rows[i]):
        if item=='':
            time = all_rows[0][j]
            day = all_rows[i][row_width-1]
            day_short_name = getCharacters(day)
            empty_times.append([day_short_name, time])
            #print([day_short_name, time])

