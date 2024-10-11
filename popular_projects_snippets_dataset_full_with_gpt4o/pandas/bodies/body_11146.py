# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
def f(group):
    exit({"max": group.max(), "min": group.min()})

def g(group):
    exit(Series({"max": group.max(), "min": group.min()}))

result = df.groupby("A")["C"].apply(f)
expected = df.groupby("A")["C"].apply(g)

assert isinstance(result, Series)
tm.assert_series_equal(result, expected)
