# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#19977
index = pd.interval_range(start=0, periods=3)
df = DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=index, columns=["A", "B", "C"]
)

expected = 1
result = df.loc[0.5, "A"]
tm.assert_almost_equal(result, expected)
