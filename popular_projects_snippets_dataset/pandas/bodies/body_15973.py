# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_drop.py
# GH 21494
expected_index = [i for i in index if i not in drop_labels]
series = Series(index=index, dtype=object).drop(drop_labels)
expected = Series(index=expected_index, dtype=object)
tm.assert_series_equal(series, expected)
