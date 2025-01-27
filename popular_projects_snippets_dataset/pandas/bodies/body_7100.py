# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py

idx = simple_index
tm.assert_index_equal(eval(repr(idx)), idx)
