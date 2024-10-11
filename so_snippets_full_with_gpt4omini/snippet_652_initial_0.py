import pandas as pd # pragma: no cover

df = pd.DataFrame(columns=['A', 'B', 'C']) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11067027/sorting-columns-in-pandas-dataframe-based-on-column-name
from l3.Runtime import _l_
df.sort_index(axis=1, inplace=True)
_l_(2324)

