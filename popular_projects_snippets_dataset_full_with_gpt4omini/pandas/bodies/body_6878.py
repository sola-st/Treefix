# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_common.py
# GH17271
index = index_flat
# not implemented for tuple searches in MultiIndex
# or Intervals searches in IntervalIndex
if isinstance(index, pd.IntervalIndex):
    mark = pytest.mark.xfail(
        reason="IntervalIndex.searchsorted does not support Interval arg",
        raises=NotImplementedError,
    )
    request.node.add_marker(mark)

# nothing to test if the index is empty
if index.empty:
    pytest.skip("Skip check for empty Index")
value = index[0]

# determine the expected results (handle dupes for 'right')
expected_left, expected_right = 0, (index == value).argmin()
if expected_right == 0:
    # all values are the same, expected_right should be length
    expected_right = len(index)

# test _searchsorted_monotonic in all cases
# test searchsorted only for increasing
if index.is_monotonic_increasing:
    ssm_left = index._searchsorted_monotonic(value, side="left")
    assert expected_left == ssm_left

    ssm_right = index._searchsorted_monotonic(value, side="right")
    assert expected_right == ssm_right

    ss_left = index.searchsorted(value, side="left")
    assert expected_left == ss_left

    ss_right = index.searchsorted(value, side="right")
    assert expected_right == ss_right

elif index.is_monotonic_decreasing:
    ssm_left = index._searchsorted_monotonic(value, side="left")
    assert expected_left == ssm_left

    ssm_right = index._searchsorted_monotonic(value, side="right")
    assert expected_right == ssm_right
else:
    # non-monotonic should raise.
    msg = "index must be monotonic increasing or decreasing"
    with pytest.raises(ValueError, match=msg):
        index._searchsorted_monotonic(value, side="left")
