# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked_shared.py
# GH#45622
arr = pd.array([1, 2, pd.NA], dtype=dtype)
other = np.arange(3, dtype=np.int64).view("m8[ns]")

result = arr * other
expected = pd.array([pd.Timedelta(0), pd.Timedelta(2), pd.NaT])
tm.assert_extension_array_equal(result, expected)
