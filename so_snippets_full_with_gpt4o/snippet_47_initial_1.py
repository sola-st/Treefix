import pandas as pd # pragma: no cover

df = pd.DataFrame({'x':[1, 2, 3], 'y':[4, 5, 6], 'z':[7, 8, 9]}) # pragma: no cover
df.columns = ['x', 'y', 'z'] # pragma: no cover
def rename(columns, axis, inplace): # pragma: no cover
    if inplace: # pragma: no cover
        df.columns = [columns[col] if col in columns else col for col in df.columns] # pragma: no cover
df.rename = rename # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11346283/renaming-column-names-in-pandas
from l3.Runtime import _l_
new_cols = ['a', 'b', 'c', 'd', 'e']
_l_(12197)
new_names_map = {df.columns[i]:new_cols[i] for i in range(len(new_cols))}
_l_(12198)

df.rename(new_names_map, axis=1, inplace=True)
_l_(12199)

