import pandas as pd # pragma: no cover

p_file = 'path/to/your/file.csv' # pragma: no cover
pd.read_csv = type('MockReadCSV', (object,), {'__call__': lambda self, *args, **kwargs: pd.DataFrame()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/24251219/pandas-read-csv-low-memory-and-dtype-options
from l3.Runtime import _l_
dashboard_df = pd.read_csv(p_file, sep=';', error_bad_lines=False, index_col=False, dtype='unicode')
_l_(1452)

