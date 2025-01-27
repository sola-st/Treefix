# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH 20416
expected = df_cat.groupby(["A", "B"])["C"].mean()
result = df_cat.groupby(["A", "B"]).mean()["C"]
tm.assert_series_equal(result, expected)
