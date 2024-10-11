# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py

f = lambda x: x.sum()
results = df.C.groupby([df.A, df.B]).aggregate(f)
expected = df.groupby(["A", "B"]).sum()["C"]
tm.assert_series_equal(results, expected)
