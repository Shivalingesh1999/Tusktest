[25-08 16:40] Sheelavantar, Shivalingesh (Nokia - IN/Bangalore)
import csv
mydict=[]
# name of csv file
#to get the header of the file
filename = open('Trace_DL_cell_1.csv', 'r')
# list to store the names of columns
list_of_column_names = []
next(filename)
# creating dictreaer object
csv_reader = csv.reader(filename, delimiter = ',')    # loop to iterate through the rows of csv
for row in csv_reader:        # adding the first row        list_of_column_names.append(row)        break
# printing the result
header=list_of_column_names[0]
filename = open('Trace_DL_cell_1.csv', 'r')
next(filename)
# creating dictreader object
file = csv.DictReader(filename)
filename = "output_2.csv"

with open(filename, 'w', newline='') as csvfile:    # creatig a csv dict writer object            writer = csv.DictWriter(csvfile, fieldnames = header)

            writer.writeheader()            for col in file:                               if (( col['ETtiTraceDlParUe_cRnti'] != '-') and (col['ETtiTraceDlParCell_cellId'] == '1' )) :                                    writer.writerows([col])
csvfile.close()


#Groupby code using csv reader
#This conerting without pandas
#df2 = df1.groupby('ETtiTraceUlParUe_cRnti').size().groupby(level=0).max().reset_index(name='counts')

def group_by_fun(file_name, column_name)
    
    filename = "/home/ute/Desktop/test/datascsv.csv"
        with open(filename, "r") as f:
            reader = csv.DictReader(f, delimiter=",")
            patient_dict = {}
            for line in reader:
                key = line['Department ']
                if key not in patient_dict:
                    patient_dict[key] = 1
                else:
                    patient_dict[key] += 1
        res = (sorted(patient_dict, key=lambda k: patient_dict[k], reverse=True))
        
    return res   
   
   
   #Changed modified now
