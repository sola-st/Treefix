# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-pandas-and-concatenate-into-one-dataframe
from l3.Runtime import _l_
try:
    import os
    _l_(14100)

except ImportError:
    pass
try:
    import glob
    _l_(14102)

except ImportError:
    pass
try:
    import pandas
    _l_(14104)

except ImportError:
    pass
try:
    from collections import OrderedDict
    _l_(14106)

except ImportError:
    pass
path =r'C:\DRO\DCL_rawdata_files'
_l_(14107)
filenames = glob.glob(path + "/*.csv")
_l_(14108)

dict_of_df = OrderedDict((f, pandas.read_csv(f)) for f in filenames)
_l_(14109)
pandas.concat(dict_of_df, sort=True)
_l_(14110)

