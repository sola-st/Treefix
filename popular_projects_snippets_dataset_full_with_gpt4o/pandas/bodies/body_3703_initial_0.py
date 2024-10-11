import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

datetime_frame = pd.DataFrame(np.random.randn(20, 3), index=pd.date_range('1/1/2000', periods=20), columns=['A', 'B', 'C']) # pragma: no cover
Series = pd.Series # pragma: no cover
tm = type('Mock', (object,), {'assert_almost_equal': lambda x, y: None, 'assert_series_equal': lambda x, y: None}) # pragma: no cover
DataFrame = pd.DataFrame # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
from l3.Runtime import _l_
a = datetime_frame
_l_(21386)
noise = Series(np.random.randn(len(a)), index=a.index)
_l_(21387)

b = datetime_frame.add(noise, axis=0)
_l_(21388)

# make sure order does not matter
b = b.reindex(columns=b.columns[::-1], index=b.index[::-1][10:])
_l_(21389)
del b["B"]
_l_(21390)

colcorr = a.corrwith(b, axis=0)
_l_(21391)
tm.assert_almost_equal(colcorr["A"], a["A"].corr(b["A"]))
_l_(21392)

rowcorr = a.corrwith(b, axis=1)
_l_(21393)
tm.assert_series_equal(rowcorr, a.T.corrwith(b.T, axis=0))
_l_(21394)

dropped = a.corrwith(b, axis=0, drop=True)
_l_(21395)
tm.assert_almost_equal(dropped["A"], a["A"].corr(b["A"]))
_l_(21396)
assert "B" not in dropped
_l_(21397)

dropped = a.corrwith(b, axis=1, drop=True)
_l_(21398)
assert a.index[-1] not in dropped.index
_l_(21399)

# non time-series data
index = ["a", "b", "c", "d", "e"]
_l_(21400)
columns = ["one", "two", "three", "four"]
_l_(21401)
df1 = DataFrame(np.random.randn(5, 4), index=index, columns=columns)
_l_(21402)
df2 = DataFrame(np.random.randn(4, 4), index=index[:4], columns=columns)
_l_(21403)
correls = df1.corrwith(df2, axis=1)
_l_(21404)
for row in index[:4]:
    _l_(21406)

    tm.assert_almost_equal(correls[row], df1.loc[row].corr(df2.loc[row]))
    _l_(21405)
