import pandas as pd # pragma: no cover

DATA = pd.DataFrame({'column1': [1, 2, 3], 'column2': ['a', 'b', 'c']}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/19828822/how-to-check-whether-a-pandas-dataframe-is-empty
from l3.Runtime import _l_
DATA is not None and isinstance(DATA, pd.DataFrame) and not DATA.empty
_l_(89)

