# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
# GH#17198
# GH#24600
result = df.quantile()
expected = expected.astype("Sparse[float]")
tm.assert_series_equal(result, expected)
