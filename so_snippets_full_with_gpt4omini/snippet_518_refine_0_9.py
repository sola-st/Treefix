import pandas as pd # pragma: no cover

df = pd.DataFrame({'A': [1, 1, 1, 2, 2, 2], 'B': ['x', 'x', 'y', 'y', 'z', 'z'], 'C': ['C', 'C', 'D', 'D', 'C', 'D'], 'E': [100, 200, 300, 400, 500, 600]}) # pragma: no cover
rows = ['A', 'B'] # pragma: no cover
cols = ['C'] # pragma: no cover
vals = 'E' # pragma: no cover
aggfuncs = 'sum' # pragma: no cover

import pandas as pd # pragma: no cover

df = pd.DataFrame({'A': [1, 1, 1, 2, 2, 2], 'B': ['x', 'y', 'x', 'y', 'z', 'z'], 'C': ['C', 'C', 'D', 'D', 'C', 'D'], 'E': [100, 200, 300, 400, 500, 600]}) # pragma: no cover
rows = ['A', 'B'] # pragma: no cover
cols = ['C'] # pragma: no cover
vals = 'E' # pragma: no cover
aggfuncs = 'sum' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/47152691/how-can-i-pivot-a-dataframe
from l3.Runtime import _l_
df.groupby(rows+cols)[vals].agg(aggfuncs).unstack(cols)
_l_(1623)
# equivalently,
df.pivot_table(vals, rows, cols, aggfuncs)
_l_(1624)

df.set_index(rows+cols)[vals].unstack(cols)
_l_(1625)
# equivalently, 
df.pivot(rows, cols, vals)
_l_(1626)

df = pd.DataFrame({'A': [1, 1, 1, 2, 2, 2], 'B': [*'xxyyzz'], 
                   'C': [*'CCDCDD'], 'E': [100, 200, 300, 400, 500, 600]})
_l_(1627)
rows, cols, vals = ['A', 'B'], ['C'], 'E'
_l_(1628)

# using pivot syntax
df1 = (
    df.assign(ix=df.groupby(rows+cols).cumcount())
    .pivot([*rows, 'ix'], cols, vals)
    .fillna(0, downcast='infer')
    .droplevel(-1).reset_index().rename_axis(columns=None)
)
_l_(1629)

# equivalently, using set_index + unstack syntax
df1 = (
    df
    .set_index([*rows, df.groupby(rows+cols).cumcount(), *cols])[vals]
    .unstack(fill_value=0)
    .droplevel(-1).reset_index().rename_axis(columns=None)
)
_l_(1630)

df1 = (
    df.assign(ix=df.groupby(rows+cols).cumcount())
    .pivot(rows, [*cols, 'ix'])[vals]
    .fillna(0, downcast='infer')
)
_l_(1631)
df1 = df1.set_axis([f"{c[0]}_{c[1]}" for c in df1], axis=1).reset_index()
_l_(1632)

# equivalently, using the set_index + unstack syntax
df1 = (
    df
    .set_index([*rows, df.groupby(rows+cols).cumcount(), *cols])[vals]
    .unstack([-1, *range(-2, -len(cols)-2, -1)], fill_value=0)
)
_l_(1633)
df1 = df1.set_axis([f"{c[0]}_{c[1]}" for c in df1], axis=1).reset_index()
_l_(1634)

df1 = df.set_index(['A', df.groupby('A').cumcount()])['E'].unstack(fill_value=0).add_prefix('Col').reset_index()
_l_(1635)

pv_1 = df.pivot_table(index=rows, columns=cols, values=vals, aggfunc=aggfuncs, fill_value=0)
_l_(1636)
# internal operation of `pivot_table()`
gb_1 = df.groupby(rows+cols)[vals].agg(aggfuncs).unstack(cols).fillna(0, downcast="infer")
_l_(1637)
pv_1.equals(gb_1) # True
_l_(1638) # True

