# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# Ensure that DatetimeArray._ndarray.base isn't lost.
arr = np.array(["2000-01-01", "2000-01-02"], dtype="M8[ns]")
dta = DatetimeArray(arr)

assert dta._ndarray is arr
dta = DatetimeArray(arr[:0])
assert dta._ndarray.base is arr
