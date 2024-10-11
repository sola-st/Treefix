import pandas as pd # pragma: no cover

import pandas as pd # pragma: no cover

# Replace 'display.height' with 'display.max_info_rows' which is a valid option# pragma: no cover
pd.set_option('display.max_info_rows', 1000) # pragma: no cover

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

