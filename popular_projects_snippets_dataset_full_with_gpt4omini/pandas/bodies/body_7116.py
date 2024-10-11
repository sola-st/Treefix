# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# GH 11343
if len(index) == 0:
    exit()
elif index.dtype == bool:
    # can't hold NAs
    exit()
elif isinstance(index, NumericIndex) and is_integer_dtype(index.dtype):
    exit()
elif isinstance(index, MultiIndex):
    idx = index.copy(deep=True)
    msg = "isna is not defined for MultiIndex"
    with pytest.raises(NotImplementedError, match=msg):
        idx.fillna(idx[0])
else:
    idx = index.copy(deep=True)
    result = idx.fillna(idx[0])
    tm.assert_index_equal(result, idx)
    assert result is not idx

    msg = "'value' must be a scalar, passed: "
    with pytest.raises(TypeError, match=msg):
        idx.fillna([idx[0]])

    idx = index.copy(deep=True)
    values = idx._values

    values[1] = np.nan

    idx = type(index)(values)

    msg = "does not support 'downcast'"
    with pytest.raises(NotImplementedError, match=msg):
        # For now at least, we only raise if there are NAs present
        idx.fillna(idx[0], downcast="infer")

    expected = np.array([False] * len(idx), dtype=bool)
    expected[1] = True
    tm.assert_numpy_array_equal(idx._isnan, expected)
    assert idx.hasnans is True
