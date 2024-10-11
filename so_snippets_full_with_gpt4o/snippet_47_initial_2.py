import pandas as pd # pragma: no cover

df = pd.DataFrame(columns=['col1', 'col2', 'col3', 'col4', 'col5']) # pragma: no cover
df.columns = pd.Index(['col1', 'col2', 'col3', 'col4', 'col5']) # pragma: no cover
df.rename = lambda new_names_map, axis, inplace: df.columns.map(lambda col: new_names_map.get(col, col)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11346283/renaming-column-names-in-pandas
from l3.Runtime import _l_
new_cols = ['a', 'b', 'c', 'd', 'e']
_l_(12197)
new_names_map = {df.columns[i]:new_cols[i] for i in range(len(new_cols))}
_l_(12198)

df.rename(new_names_map, axis=1, inplace=True)
_l_(12199)

