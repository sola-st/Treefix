# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
a = Index([3, Timestamp("2000"), 1])
b = Index([2, Timestamp("1999"), 1])
op = operator.methodcaller(opname, b)

with tm.assert_produces_warning(RuntimeWarning):
    # sort=None, the default
    result = op(a)
expected = Index([3, Timestamp("2000"), 2, Timestamp("1999")])
if opname == "difference":
    expected = expected[:2]
tm.assert_index_equal(result, expected)

# sort=False
op = operator.methodcaller(opname, b, sort=False)
result = op(a)
tm.assert_index_equal(result, expected)
