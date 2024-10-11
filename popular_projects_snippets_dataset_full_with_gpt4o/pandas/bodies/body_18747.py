# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    Fixture for tests on indexes, series and series with a narrow dtype
    copy to avoid mutation, e.g. setting .name
    """
exit(_index_or_series_objs[request.param].copy(deep=True))
