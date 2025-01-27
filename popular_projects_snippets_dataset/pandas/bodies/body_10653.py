# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_min_max.py
# GH 31471
groups = [1, 2]
periods = pd.period_range("2020", periods=2, freq="Y")
df = DataFrame({"a": groups, "b": periods})

result = getattr(df.groupby("a")["b"], func)()
idx = Index([1, 2], name="a")
expected = Series(periods, index=idx, name="b")

tm.assert_series_equal(result, expected)
