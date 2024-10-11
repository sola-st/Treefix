# Extracted from ./data/repos/pandas/pandas/tests/series/test_ufunc.py
box = box_with_array
values = values_for_np_reduce

with tm.assert_produces_warning(None):
    obj = box(values)

if isinstance(values, pd.core.arrays.SparseArray):
    mark = pytest.mark.xfail(reason="SparseArray has no 'prod'")
    request.node.add_marker(mark)

if values.dtype.kind in "iuf":
    result = np.multiply.reduce(obj)
    if box is pd.DataFrame:
        expected = obj.prod(numeric_only=False)
        tm.assert_series_equal(result, expected)
    elif box is pd.Index:
        # Index has no 'prod'
        expected = obj._values.prod()
        assert result == expected
    else:

        expected = obj.prod()
        assert result == expected
else:
    msg = "|".join(
        [
            "does not support reduction",
            "unsupported operand type",
            "ufunc 'multiply' cannot use operands",
        ]
    )
    with pytest.raises(TypeError, match=msg):
        np.multiply.reduce(obj)
