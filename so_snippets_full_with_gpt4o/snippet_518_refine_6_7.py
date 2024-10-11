import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

df = pd.DataFrame({'A': [1, 1, 1, 2, 2, 2], 'B': ['x', 'x', 'y', 'y', 'z', 'z'], 'C': ['C', 'C', 'D', 'C', 'D', 'D'], 'E': [100, 200, 300, 400, 500, 600]}) # pragma: no cover
rows, cols, vals = ['A', 'B'], ['C'], 'E' # pragma: no cover
aggfuncs = np.sum # pragma: no cover

import pandas as pd # pragma: no cover

df = pd.DataFrame({'A': [1, 1, 3, 2, 2, 4], 'B': ['x', 'x', 'y', 'y', 'z', 'w'], 'C': ['C', 'D', 'D', 'C', 'D', 'C'], 'E': [100, 200, 300, 400, 500, 600]}) # pragma: no cover
rows = ['A', 'B'] # pragma: no cover
cols = ['C'] # pragma: no cover
vals = 'E' # pragma: no cover
aggfuncs = 'sum' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/47152691/how-can-i-pivot-a-dataframe
from l3.Runtime import _l_
df.groupby(rows+cols)[vals].agg(aggfuncs).unstack(cols)
_l_(14146)
# equivalently,
df.pivot_table(vals, rows, cols, aggfuncs)
_l_(14147)

df.set_index(rows+cols)[vals].unstack(cols)
_l_(14148)
# equivalently, 
df.pivot(rows, cols, vals)
_l_(14149)

df = pd.DataFrame({'A': [1, 1, 1, 2, 2, 2], 'B': [*'xxyyzz'], 
                   'C': [*'CCDCDD'], 'E': [100, 200, 300, 400, 500, 600]})
_l_(14150)
rows, cols, vals = ['A', 'B'], ['C'], 'E'
_l_(14151)

# using pivot syntax
df1 = (
    df.assign(ix=df.groupby(rows+cols).cumcount())
    .pivot([*rows, 'ix'], cols, vals)
    .fillna(0, downcast='infer')
    .droplevel(-1).reset_index().rename_axis(columns=None)
)
_l_(14152)

# equivalently, using set_index + unstack syntax
df1 = (
    df
    .set_index([*rows, df.groupby(rows+cols).cumcount(), *cols])[vals]
    .unstack(fill_value=0)
    .droplevel(-1).reset_index().rename_axis(columns=None)
)
_l_(14153)

df1 = (
    df.assign(ix=df.groupby(rows+cols).cumcount())
    .pivot(rows, [*cols, 'ix'])[vals]
    .fillna(0, downcast='infer')
)
_l_(14154)
df1 = df1.set_axis([f"{c[0]}_{c[1]}" for c in df1], axis=1).reset_index()
_l_(14155)

# equivalently, using the set_index + unstack syntax
df1 = (
    df
    .set_index([*rows, df.groupby(rows+cols).cumcount(), *cols])[vals]
    .unstack([-1, *range(-2, -len(cols)-2, -1)], fill_value=0)
)
_l_(14156)
df1 = df1.set_axis([f"{c[0]}_{c[1]}" for c in df1], axis=1).reset_index()
_l_(14157)

df1 = df.set_index(['A', df.groupby('A').cumcount()])['E'].unstack(fill_value=0).add_prefix('Col').reset_index()
_l_(14158)

pv_1 = df.pivot_table(index=rows, columns=cols, values=vals, aggfunc=aggfuncs, fill_value=0)
_l_(14159)
# internal operation of `pivot_table()`
gb_1 = df.groupby(rows+cols)[vals].agg(aggfuncs).unstack(cols).fillna(0, downcast="infer")
_l_(14160)
pv_1.equals(gb_1) # True
_l_(14161) # True

