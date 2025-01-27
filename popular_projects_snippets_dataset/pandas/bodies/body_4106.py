# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH 19976
data = DataFrame(data)

if any(is_categorical_dtype(x) for x in data.dtypes):
    with pytest.raises(
        TypeError, match="dtype category does not support reduction"
    ):
        func(data)

    # method version
    with pytest.raises(
        TypeError, match="dtype category does not support reduction"
    ):
        getattr(DataFrame(data), func.__name__)(axis=None)
else:
    result = func(data)
    assert isinstance(result, np.bool_)
    assert result.item() is expected

    # method version
    result = getattr(DataFrame(data), func.__name__)(axis=None)
    assert isinstance(result, np.bool_)
    assert result.item() is expected
