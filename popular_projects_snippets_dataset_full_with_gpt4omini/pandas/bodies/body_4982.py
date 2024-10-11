# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# GH 17927
# mode tries to sort multimodal series.
# Complex numbers are sorted by their magnitude
result = Series(array, dtype=dtype).mode()
tm.assert_series_equal(result, expected)
