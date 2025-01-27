# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH 15077 empty DataFrame
df = DataFrame({"x": [1, 2, 3], "y": [1.0, 2.0, 3.0]})
const = 2

empty = df.iloc[:0]
result = getattr(empty, opname)(const).dtypes.value_counts()
tm.assert_series_equal(result, Series([2], index=[np.dtype(bool)]))
