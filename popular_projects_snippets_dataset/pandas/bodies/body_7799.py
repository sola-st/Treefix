# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
# doesn't quite fit into check_sort_values_without_freq
idx = PeriodIndex(["2011", "2013", "NaT", "2011"], name="pidx", freq="D")
expected = PeriodIndex(["NaT", "2011", "2011", "2013"], name="pidx", freq="D")

ordered = idx.sort_values(na_position="first")
tm.assert_index_equal(ordered, expected)
check_freq_nonmonotonic(ordered, idx)

ordered = idx.sort_values(ascending=False)
tm.assert_index_equal(ordered, expected[::-1])
check_freq_nonmonotonic(ordered, idx)
