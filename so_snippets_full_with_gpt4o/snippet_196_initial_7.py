import pandas as pd # pragma: no cover

pd = pd # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/19124601/pretty-print-an-entire-pandas-series-dataframe
from l3.Runtime import _l_
pd.set_option('display.height',1000)
_l_(12625)
pd.set_option('display.max_rows',500)
_l_(12626)
pd.set_option('display.max_columns',500)
_l_(12627)
pd.set_option('display.width',1000)
_l_(12628)

