# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# operations
df = DataFrame({"A": np.arange(10), "B": np.random.rand(10)})
expected = getattr(df, op)(df)
expected.columns = ["A", "A"]
df.columns = ["A", "A"]
result = getattr(df, op)(df)
tm.assert_frame_equal(result, expected)
str(result)
result.dtypes
