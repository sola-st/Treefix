import pandas as pd # pragma: no cover

data = {'col1': [1, 2], 'col2': [3, 4], 'col3': [5, 6], 'col4': [7, 8], 'col5': [9, 10]} # pragma: no cover
df = pd.DataFrame(data) # pragma: no cover
df.rename = type('Mock', (object,), {'rename': lambda self, cols, axis, inplace: self})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11346283/renaming-column-names-in-pandas
from l3.Runtime import _l_
new_cols = ['a', 'b', 'c', 'd', 'e']
_l_(12197)
new_names_map = {df.columns[i]:new_cols[i] for i in range(len(new_cols))}
_l_(12198)

df.rename(new_names_map, axis=1, inplace=True)
_l_(12199)

