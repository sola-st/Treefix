# Extracted from ./data/repos/pandas/pandas/tests/series/test_iteration.py
for i, val in enumerate(datetime_series):
    # pylint: disable-next=unnecessary-list-index-lookup
    assert val == datetime_series[i]
