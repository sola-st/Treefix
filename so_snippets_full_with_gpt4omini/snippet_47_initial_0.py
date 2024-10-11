import pandas as pd # pragma: no cover

df = pd.DataFrame(columns=['a', 'b', 'c', 'd', 'e']) # pragma: no cover
df.columns = ['a', 'b', 'c', 'd', 'e'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11346283/renaming-column-names-in-pandas
from l3.Runtime import _l_
new_cols = ['a', 'b', 'c', 'd', 'e']
_l_(602)
new_names_map = {df.columns[i]:new_cols[i] for i in range(len(new_cols))}
_l_(603)

df.rename(new_names_map, axis=1, inplace=True)
_l_(604)

