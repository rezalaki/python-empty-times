import string
import random
from openpyxl import Workbook
from random import randint


cletters = [] #capital letters array
for letter in string.ascii_uppercase:
   cletters.append(letter)
   if letter=="G":
       break


#days of week
week_days = ['', '' , '', 'Saturday', 'Sunday', 'Monday','Tuesday' ,'Wednesday', 'Thursday', 'Friday']

#courses with some empty times
courses = ['course A', 'course B', '','', 'course D','','course F','course G','','course Q','course W','']

def run():
    wb = Workbook()
    cell = wb.active

    #class times
    times = ['20-18', '18-16', '16-14' , '14-12' , '12-10' , '10-8', 'days/times']

    for index, col in enumerate(cletters):
        for i in range(1,8):
            data = random.choice(courses) #choose from courses array randomly
            if i==1:
                data=""
            elif i==2:
                data = times[index]
            elif col=='G':
                data = week_days[i]
                
            dir = col + str(i)
            cell[dir] = data

    rnd_number = randint(100,999)
    target_directory = "data_store" + "/"
    file_name = "test_file_"+ str(rnd_number) +".xlsx"
    wb.save(target_directory + file_name)


# create 5 fake excel files for testing
for i in range(0, 5):
    run()



