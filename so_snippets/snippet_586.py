# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/24251219/pandas-read-csv-low-memory-and-dtype-options
from l3.Runtime import _l_
dashboard_df = pd.read_csv(p_file, sep=';', error_bad_lines=False, index_col=False, dtype='unicode')
_l_(1452)

