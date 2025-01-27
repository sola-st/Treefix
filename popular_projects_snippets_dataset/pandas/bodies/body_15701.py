# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_add_prefix_suffix.py
with_prefix = string_series.add_prefix("foo#")
expected = Index([f"foo#{c}" for c in string_series.index])
tm.assert_index_equal(with_prefix.index, expected)

with_suffix = string_series.add_suffix("#foo")
expected = Index([f"{c}#foo" for c in string_series.index])
tm.assert_index_equal(with_suffix.index, expected)

with_pct_prefix = string_series.add_prefix("%")
expected = Index([f"%{c}" for c in string_series.index])
tm.assert_index_equal(with_pct_prefix.index, expected)

with_pct_suffix = string_series.add_suffix("%")
expected = Index([f"{c}%" for c in string_series.index])
tm.assert_index_equal(with_pct_suffix.index, expected)
