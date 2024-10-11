import pandas as pd # pragma: no cover

data1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/20490274/how-to-reset-index-in-a-pandas-dataframe
from l3.Runtime import _l_
data1.reset_index(inplace=True)
_l_(13745)

