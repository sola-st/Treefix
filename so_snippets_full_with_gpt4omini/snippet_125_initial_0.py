import pandas as pd # pragma: no cover

df = pd.DataFrame({'mean': [1, 2, 3], 'A': [4, 5, 6], 'B': [7, 8, 9]}) # pragma: no cover
df.columns = ['mean', 'A', 'B'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/13148429/how-to-change-the-order-of-dataframe-columns
from l3.Runtime import _l_
df = df[['mean'] + df.columns[:-1].tolist()]
_l_(2201)

