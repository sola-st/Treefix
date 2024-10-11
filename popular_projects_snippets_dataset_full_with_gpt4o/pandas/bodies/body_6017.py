# Extracted from ./data/repos/pandas/pandas/tests/extension/test_numpy.py
"""
    Tests for PandasArray with nested data. Users typically won't create
    these objects via `pd.array`, but they can show up through `.array`
    on a Series with nested data. Many of the base tests fail, as they aren't
    appropriate for nested data.

    This fixture allows these tests to be skipped when used as a usefixtures
    marker to either an individual test or a test class.
    """
if dtype == "object":
    mark = pytest.mark.xfail(reason="Fails for object dtype")
    request.node.add_marker(mark)
