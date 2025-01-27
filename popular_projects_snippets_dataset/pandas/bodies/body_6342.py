# Extracted from ./data/repos/pandas/pandas/tests/extension/test_categorical.py
# GH 28668
result = expected.astype("category").astype(expected.dtype)

tm.assert_series_equal(result, expected)
