# Extracted from ./data/repos/pandas/pandas/util/_test_decorators.py
mark = pytest.mark.xfail(reason="Not yet implemented for ArrayManager")
request.node.add_marker(mark)
