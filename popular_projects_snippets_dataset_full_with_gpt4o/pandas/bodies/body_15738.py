# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_asof.py
from pandas import (
    PeriodIndex,
    period_range,
)

# array or list or dates
N = 50
rng = period_range("1/1/1990", periods=N, freq="H")
ts = Series(np.random.randn(N), index=rng)
ts.iloc[15:30] = np.nan
dates = date_range("1/1/1990", periods=N * 3, freq="37min")

result = ts.asof(dates)
assert notna(result).all()
lb = ts.index[14]
ub = ts.index[30]

result = ts.asof(list(dates))
assert notna(result).all()
lb = ts.index[14]
ub = ts.index[30]

pix = PeriodIndex(result.index.values, freq="H")
mask = (pix >= lb) & (pix < ub)
rs = result[mask]
assert (rs == ts[lb]).all()

ts.iloc[5:10] = np.nan
ts.iloc[15:20] = np.nan

val1 = ts.asof(ts.index[7])
val2 = ts.asof(ts.index[19])

assert val1 == ts[4]
assert val2 == ts[14]

# accepts strings
val1 = ts.asof(str(ts.index[7]))
assert val1 == ts[4]

# in there
assert ts.asof(ts.index[3]) == ts[3]

# no as of value
d = ts.index[0].to_timestamp() - offsets.BDay()
assert isna(ts.asof(d))

# Mismatched freq
msg = "Input has different freq"
with pytest.raises(IncompatibleFrequency, match=msg):
    ts.asof(rng.asfreq("D"))
