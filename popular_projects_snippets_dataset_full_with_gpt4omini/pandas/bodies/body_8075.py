# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
n = len(index)
drop = index[list(range(5, 10))]
dropped = index.drop(drop)

expected = index[list(range(5)) + list(range(10, n))]
tm.assert_index_equal(dropped, expected)

dropped = index.drop(index[0])
expected = index[1:]
tm.assert_index_equal(dropped, expected)
