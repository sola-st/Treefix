# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
from l3.Runtime import _l_
a = datetime_frame
_l_(10332)
noise = Series(np.random.randn(len(a)), index=a.index)
_l_(10333)

b = datetime_frame.add(noise, axis=0)
_l_(10334)

# make sure order does not matter
b = b.reindex(columns=b.columns[::-1], index=b.index[::-1][10:])
_l_(10335)
del b["B"]
_l_(10336)

colcorr = a.corrwith(b, axis=0)
_l_(10337)
tm.assert_almost_equal(colcorr["A"], a["A"].corr(b["A"]))
_l_(10338)

rowcorr = a.corrwith(b, axis=1)
_l_(10339)
tm.assert_series_equal(rowcorr, a.T.corrwith(b.T, axis=0))
_l_(10340)

dropped = a.corrwith(b, axis=0, drop=True)
_l_(10341)
tm.assert_almost_equal(dropped["A"], a["A"].corr(b["A"]))
_l_(10342)
assert "B" not in dropped
_l_(10343)

dropped = a.corrwith(b, axis=1, drop=True)
_l_(10344)
assert a.index[-1] not in dropped.index
_l_(10345)

# non time-series data
index = ["a", "b", "c", "d", "e"]
_l_(10346)
columns = ["one", "two", "three", "four"]
_l_(10347)
df1 = DataFrame(np.random.randn(5, 4), index=index, columns=columns)
_l_(10348)
df2 = DataFrame(np.random.randn(4, 4), index=index[:4], columns=columns)
_l_(10349)
correls = df1.corrwith(df2, axis=1)
_l_(10350)
for row in index[:4]:
    _l_(10352)

    tm.assert_almost_equal(correls[row], df1.loc[row].corr(df2.loc[row]))
    _l_(10351)
