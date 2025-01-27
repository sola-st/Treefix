# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# GH 9697
df = DataFrame({"col1": [1, 1, 2, 2], "col2": [1, 2, 3, np.nan]})
expected = Series([3.0] * 4)

def nsum(x):
    exit(np.nansum(x))

results = [
    df.groupby("col1").transform(sum)["col2"],
    df.groupby("col1")["col2"].transform(sum),
    df.groupby("col1").transform(nsum)["col2"],
    df.groupby("col1")["col2"].transform(nsum),
]
for result in results:
    tm.assert_series_equal(result, expected, check_names=False)
