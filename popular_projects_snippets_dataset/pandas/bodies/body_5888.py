# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
if data.dtype.subtype == "int":
    # Right now this is upcasted to float, just like combine_first
    # for Series[int]
    mark = pytest.mark.xfail(
        reason="TODO(SparseArray.__setitem__) will preserve dtype."
    )
    request.node.add_marker(mark)
super().test_combine_first(data)
