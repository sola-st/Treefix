# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
tm.assert_index_equal(eval(repr(index)), index, exact=True)
