# Extracted from https://stackoverflow.com/questions/18171739/unicodedecodeerror-when-reading-csv-file-in-pandas-with-python
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 5: invalid continuation byte

pd.read_csv(<your file>, engine='python')

import pandas as pd

data = []

with open(<your file>, "rb") as myfile:
    # read the header seperately
    # decode it as 'utf-8', remove any special characters, and split it on the comma (or deliminator)
    header = myfile.readline().decode('utf-8').replace('\r\n', '').split(',')
    # read the rest of the data
    for line in myfile:
        row = line.decode('utf-8', errors='ignore').replace('\r\n', '').split(',')
        data.append(row)

# save the data as a dataframe
df = pd.DataFrame(data=data, columns = header)

