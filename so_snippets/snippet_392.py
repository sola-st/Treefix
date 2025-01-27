# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/20845213/how-to-avoid-pandas-creating-an-index-in-a-saved-csv
from l3.Runtime import _l_
pd.read_csv('filename.csv', index_col='Unnamed: 0')
_l_(1802)

