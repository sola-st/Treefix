# Extracted from https://stackoverflow.com/questions/20638006/convert-list-of-dictionaries-to-a-pandas-dataframe
import csv

my file= 'C:\Users\John\Desktop\export_dataframe.csv'

records_to_save = data2 #used as in the thread. 


colnames = list[records_to_save[0].keys()] 
# remember colnames is a list of all keys. All values are written corresponding
# to the keys and "None" is specified in case of missing value 

with open(myfile, 'w', newline="",encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(colnames)
    for d in records_to_save:
        writer.writerow([d.get(r, "None") for r in colnames])

