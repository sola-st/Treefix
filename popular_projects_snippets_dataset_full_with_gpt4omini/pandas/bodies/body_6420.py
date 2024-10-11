# Extracted from ./data/repos/pandas/pandas/tests/extension/test_string.py
if isinstance(data, ArrowStringArray):
    mark = pytest.mark.xfail(
        reason="2D support not implemented for ArrowStringArray"
    )
    request.node.add_marker(mark)
