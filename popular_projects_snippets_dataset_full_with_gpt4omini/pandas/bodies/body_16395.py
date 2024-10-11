# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
ser = Series([1, 2, 3])
result = Series(ser.array)
tm.assert_series_equal(ser, result)
if not using_array_manager:
    assert isinstance(result._mgr.blocks[0], NumericBlock)
