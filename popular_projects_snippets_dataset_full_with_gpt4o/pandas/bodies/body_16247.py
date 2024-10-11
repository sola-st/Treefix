# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# TODO: share with frame test of the same name
# GH 49573 (addition of empty_index parameter)
expected = Series(index=empty_index)
result = constructor(empty_index)

assert result.dtype == object
assert len(result.index) == 0
tm.assert_series_equal(result, expected, check_index_type=check_index_type)
