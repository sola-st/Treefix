# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
# GH 21670
index = interval_range(0, 5, closed=closed, name=name)
result = index.set_closed(new_closed)
expected = interval_range(0, 5, closed=new_closed, name=name)
tm.assert_index_equal(result, expected)
