# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
index = simple_index
tm.assert_index_equal(eval(repr(index)), index)
