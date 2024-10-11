# Extracted from ./data/repos/pandas/pandas/tests/extension/test_string.py
if data.dtype.storage == "pyarrow":
    mark = pytest.mark.xfail(reason="not implemented")
    request.node.add_marker(mark)
super().test_setitem_preserves_views(data)
