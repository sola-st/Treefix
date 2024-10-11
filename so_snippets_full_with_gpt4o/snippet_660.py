# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16327055/how-to-add-an-empty-column-to-a-dataframe
from l3.Runtime import _l_
df['column'] = None #This works. This will create a new column with None type
_l_(12803) #This works. This will create a new column with None type
df.column = None #This will work only when the column is already present in the dataframe 
_l_(12804) #This will work only when the column is already present in the dataframe 

