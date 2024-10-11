# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 9114
dtype = np.dtype(f"M8[{unit}]")
base = to_datetime(["2000-01-01T00:00", "2000-01-02T00:00", "NaT"], cache=cache)

values = base.values.astype(dtype)

if unit in ["h", "m"]:
    # we cast to closest supported unit
    unit = "s"
exp_dtype = np.dtype(f"M8[{unit}]")
expected = DatetimeIndex(base.astype(exp_dtype))
assert expected.dtype == exp_dtype

tm.assert_index_equal(DatetimeIndex(values), expected)
tm.assert_index_equal(to_datetime(values, cache=cache), expected)
