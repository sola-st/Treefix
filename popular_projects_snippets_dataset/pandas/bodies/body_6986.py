# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
# TODO(GH#25151): decide on True behaviour
# # sort=True, raises
a = Index([3, Timestamp("2000"), 1])
b = Index([2, Timestamp("1999"), 1])
op = operator.methodcaller(opname, b, sort=True)

with pytest.raises(TypeError, match="Cannot compare"):
    op(a)
