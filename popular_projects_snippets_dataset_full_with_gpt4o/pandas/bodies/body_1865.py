# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py
# GH#46442 test if `numeric_only` behave as expected for DataFrameGroupBy

index = date_range("2018-01-01", periods=2, freq="D")
expected_index = date_range("2018-12-31", periods=1, freq="Y")
df = DataFrame({"cat": ["cat_1", "cat_2"], "num": [5, 20]}, index=index)
resampled = df.resample("Y")
if numeric_only is lib.no_default:
    kwargs = {}
else:
    kwargs = {"numeric_only": numeric_only}

func = getattr(resampled, method)
if isinstance(expected_data, str):
    klass = TypeError if method in ("var", "mean", "median", "prod") else ValueError
    with pytest.raises(klass, match=expected_data):
        _ = func(**kwargs)
else:
    result = func(**kwargs)
    expected = DataFrame(expected_data, index=expected_index)
    tm.assert_frame_equal(result, expected)
