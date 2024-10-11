# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/13148429/how-to-change-the-order-of-dataframe-columns
from l3.Runtime import _l_
df = df[['mean'] + df.columns[:-1].tolist()]
_l_(14431)

