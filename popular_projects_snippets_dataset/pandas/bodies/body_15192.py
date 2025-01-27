# Extracted from ./data/repos/pandas/pandas/tests/series/test_ufunc.py
box = box_with_array
values = values_for_np_reduce

with tm.assert_produces_warning(None):
    obj = box(values)

if values.dtype.kind in "miuf":
    result = np.add.reduce(obj)
    if box is pd.DataFrame:
        expected = obj.sum(numeric_only=False)
        tm.assert_series_equal(result, expected)
    elif box is pd.Index:
        # Index has no 'sum'
        expected = obj._values.sum()
        assert result == expected
    else:
        expected = obj.sum()
        assert result == expected
else:
    msg = "|".join(
        [
            "does not support reduction",
            "unsupported operand type",
            "ufunc 'add' cannot use operands",
        ]
    )
    with pytest.raises(TypeError, match=msg):
        np.add.reduce(obj)
