# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/10715965/create-a-pandas-dataframe-by-appending-one-row-at-a-time
# Assuming your df has 4 columns (str, int, str, bool)
from l3.Runtime import _l_
df.loc[df.shape[0]] = ['col1Value', 100, 'col3Value', False] 
_l_(15050) 

df.loc[len(df)] = ['col1Value', 100, 'col3Value', False] 
_l_(15051) 

