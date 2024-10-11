# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# GH#24115 check that iadd and isub are actually in-place
data = np.arange(10, dtype="i8") * 24 * 3600 * 10**9
arr = self.array_cls(data, freq="D")

expected = arr + pd.Timedelta(days=1)
arr += pd.Timedelta(days=1)
tm.assert_equal(arr, expected)

expected = arr - pd.Timedelta(days=1)
arr -= pd.Timedelta(days=1)
tm.assert_equal(arr, expected)
