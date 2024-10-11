import pandas as pd # pragma: no cover

df = pd.DataFrame(columns=['A', 'B', 'C']) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/19482970/get-a-list-from-pandas-dataframe-column-headers
from l3.Runtime import _l_
df.columns.tolist()
_l_(153)

