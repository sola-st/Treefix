# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH#2817
dtype = any_real_numpy_dtype
data = {
    "amount": {0: 700, 1: 600, 2: 222, 3: 333, 4: 444},
    "col": {0: 3.5, 1: 3.5, 2: 4.0, 3: 4.0, 4: 4.0},
    "num": {0: 12, 1: 11, 2: 12, 3: 12, 4: 12},
}
df = DataFrame(data)
df = df.astype({"col": dtype, "num": dtype})
df = df.set_index(keys=["col", "num"])
key = 4.0, 12

# emits a PerformanceWarning, ok
with tm.assert_produces_warning(PerformanceWarning):
    tm.assert_frame_equal(df.loc[key], df.iloc[2:])

# this is ok
return_value = df.sort_index(inplace=True)
assert return_value is None
res = df.loc[key]

# col has float dtype, result should be float64 Index
col_arr = np.array([4.0] * 3, dtype=dtype)
year_arr = np.array([12] * 3, dtype=dtype)
index = MultiIndex.from_arrays([col_arr, year_arr], names=["col", "num"])
expected = DataFrame({"amount": [222, 333, 444]}, index=index)
tm.assert_frame_equal(res, expected)
