# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
n = len(index)
drop = index[list(range(5, 10))]
mixed = drop.tolist() + ["foo"]
dropped = index.drop(mixed, errors="ignore")

expected = index[list(range(5)) + list(range(10, n))]
tm.assert_index_equal(dropped, expected)

dropped = index.drop(["foo", "bar"], errors="ignore")
expected = index[list(range(n))]
tm.assert_index_equal(dropped, expected)
