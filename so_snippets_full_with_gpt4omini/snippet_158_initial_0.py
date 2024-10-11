import pandas as pd # pragma: no cover

df = pd.DataFrame(columns=['col1', 'col2', 'col3', 'col4']) # pragma: no cover
pd.DataFrame.loc = type('Mock', (object,), {'__getitem__': lambda self, key: self})() # pragma: no cover
pd.DataFrame.shape = property(lambda self: (0, 4)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/10715965/create-a-pandas-dataframe-by-appending-one-row-at-a-time
# Assuming your df has 4 columns (str, int, str, bool)
from l3.Runtime import _l_
df.loc[df.shape[0]] = ['col1Value', 100, 'col3Value', False] 
_l_(2493) 

df.loc[len(df)] = ['col1Value', 100, 'col3Value', False] 
_l_(2494) 

