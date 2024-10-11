# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#19977
index = pd.interval_range(start=0, periods=3, closed="both")
df = DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=index, columns=["A", "B", "C"]
)

index_exp = pd.interval_range(start=0, periods=2, freq=1, closed="both")
expected = Series([1, 4], index=index_exp, name="A")
result = df.loc[1, "A"]
tm.assert_series_equal(result, expected)
