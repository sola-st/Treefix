# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_filters.py
df = DataFrame({"A": [1, 12, 12, 1], "B": "a b c d".split()})
grouper = df["A"].apply(lambda x: x % 2)
grouped = df.groupby(grouper)
expected = DataFrame({"A": [12, 12], "B": ["b", "c"]}, index=[1, 2])
tm.assert_frame_equal(grouped.filter(lambda x: x["A"].sum() > 10), expected)
