# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/26886653/create-new-column-based-on-values-from-other-columns-apply-a-function-of-multi
from l3.Runtime import _l_
try:
    import pandas as pd
    _l_(1751)

except ImportError:
    pass

# make a simple dataframe
df = pd.DataFrame({'a':[1,2], 'b':[3,4]})
_l_(1752)
df
_l_(1753)
#    a  b
# 0  1  3
# 1  2  4

# create an unattached column with an index
df.apply(lambda row: row.a + row.b, axis=1)
_l_(1754)
# 0    4
# 1    6

# do same but attach it to the dataframe
df['c'] = df.apply(lambda row: row.a + row.b, axis=1)
_l_(1755)
df
_l_(1756)
#    a  b  c
# 0  1  3  4
# 1  2  4  6

fn = lambda row: row.a + row.b # define a function for the new column
_l_(1757) # define a function for the new column
col = df.apply(fn, axis=1) # get column data with an index
_l_(1758) # get column data with an index
df = df.assign(c=col.values) # assign values to column 'c'
_l_(1759) # assign values to column 'c'

df = df.assign(**{'some column name': col.values})
_l_(1760)

