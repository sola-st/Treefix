# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nunique.py
# GH 27951
df = DataFrame({"key": key, "data": data})
result = df.groupby(["key"])["data"].nunique(dropna=dropna)
tm.assert_series_equal(result, expected)
