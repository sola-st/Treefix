# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/15705630/get-the-rows-which-have-the-max-value-in-groups-using-groupby
from l3.Runtime import _l_
df[df['count'] == df.groupby(['Mt'])['count'].transform(max)]
_l_(14406)

