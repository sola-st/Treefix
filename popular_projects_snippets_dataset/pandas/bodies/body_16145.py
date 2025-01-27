# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py
# GH#47500
ser = Series([0, 1, 1], dtype=dtype)
if kernel == "corrwith":
    args = (ser,)
elif kernel == "corr":
    args = (ser,)
elif kernel == "cov":
    args = (ser,)
elif kernel == "nth":
    args = (0,)
elif kernel == "fillna":
    args = (True,)
elif kernel == "fillna":
    args = ("ffill",)
elif kernel == "take":
    args = ([0],)
elif kernel == "quantile":
    args = (0.5,)
else:
    args = ()
method = getattr(ser, kernel)
if not has_numeric_only:
    msg = (
        "(got an unexpected keyword argument 'numeric_only'"
        "|too many arguments passed in)"
    )
    with pytest.raises(TypeError, match=msg):
        method(*args, numeric_only=True)
elif dtype is object:
    msg = f"Series.{kernel} does not allow numeric_only=True with non-numeric"
    with pytest.raises(TypeError, match=msg):
        method(*args, numeric_only=True)
else:
    result = method(*args, numeric_only=True)
    expected = method(*args, numeric_only=False)
    if isinstance(expected, Series):
        # transformer
        tm.assert_series_equal(result, expected)
    else:
        # reducer
        assert result == expected
