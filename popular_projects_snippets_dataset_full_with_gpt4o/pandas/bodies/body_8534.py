# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_datetime.py
# GH8943.  On some machines NumPy defaults to np.int32 (for example,
# 32-bit Linux machines).  In the function _generate_regular_range
# found in tseries/index.py, `periods` gets multiplied by `strides`
# (which has value 1e9) and since the max value for np.int32 is ~2e9,
# and since those machines won't promote np.int32 to np.int64, we get
# overflow.
periods = np.int_(1000)

idx1 = date_range(start="2000", periods=periods, freq="S")
assert len(idx1) == periods

idx2 = date_range(end="2000", periods=periods, freq="S")
assert len(idx2) == periods
