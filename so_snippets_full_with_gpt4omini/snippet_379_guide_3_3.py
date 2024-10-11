import os # pragma: no cover
import glob # pragma: no cover
import pandas as pd # pragma: no cover
from collections import OrderedDict # pragma: no cover

path = r'C:\DRO\DCL_rawdata_files' # pragma: no cover
filenames = ['file1.csv', 'file2.csv'] # pragma: no cover
dict_of_df = OrderedDict((f, pd.DataFrame({'column1': [1], 'column2': [2]})) for f in filenames) # pragma: no cover
result = pd.concat(dict_of_df.values(), sort=True) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-pandas-and-concatenate-into-one-dataframe
from l3.Runtime import _l_
try:
    import os
    _l_(1917)

except ImportError:
    pass
try:
    import glob
    _l_(1919)

except ImportError:
    pass
try:
    import pandas
    _l_(1921)

except ImportError:
    pass
try:
    from collections import OrderedDict
    _l_(1923)

except ImportError:
    pass
path =r'C:\DRO\DCL_rawdata_files'
_l_(1924)
filenames = glob.glob(path + "/*.csv")
_l_(1925)

dict_of_df = OrderedDict((f, pandas.read_csv(f)) for f in filenames)
_l_(1926)
pandas.concat(dict_of_df, sort=True)
_l_(1927)

