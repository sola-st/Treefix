# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = data.dtype.pyarrow_dtype
ser = pd.Series(data)
# pd.Series([ser.iloc[0]] * len(ser)) may not return ArrowExtensionArray
# since ser.iloc[0] is a python scalar
other = pd.Series(pd.array([ser.iloc[0]] * len(ser), dtype=data.dtype))
if comparison_op.__name__ in ["eq", "ne"]:
    # comparison should match point-wise comparisons
    result = comparison_op(ser, other)
    # Series.combine does not calculate the NA mask correctly
    # when comparing over an array
    assert result[8] is na_value
    assert result[97] is na_value
    expected = ser.combine(other, comparison_op)
    expected[8] = na_value
    expected[97] = na_value
    self.assert_series_equal(result, expected)

else:
    exc = None
    try:
        result = comparison_op(ser, other)
    except Exception as err:
        exc = err

    if exc is None:
        # Didn't error, then should match point-wise behavior
        if pa.types.is_temporal(pa_dtype):
            # point-wise comparison with pd.NA raises TypeError
            assert result[8] is na_value
            assert result[97] is na_value
            result = result.drop([8, 97]).reset_index(drop=True)
            ser = ser.drop([8, 97])
            other = other.drop([8, 97])
        expected = ser.combine(other, comparison_op)
        self.assert_series_equal(result, expected)
    else:
        with pytest.raises(type(exc)):
            ser.combine(other, comparison_op)
