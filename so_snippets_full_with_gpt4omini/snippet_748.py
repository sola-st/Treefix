# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/26414913/normalize-columns-of-a-dataframe
from l3.Runtime import _l_
df = df/df.max().astype(np.float64)
_l_(1045)

df = df/df.loc[df.abs().idxmax()].astype(np.float64)
_l_(1046)

