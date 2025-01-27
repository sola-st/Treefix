# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py
# GH#46442 test if `numeric_only` behave as expected for SeriesGroupBy

index = date_range("2018-01-01", periods=2, freq="D")
expected_index = date_range("2018-12-31", periods=1, freq="Y")
df = Series(["cat_1", "cat_2"], index=index)
resampled = df.resample("Y")
kwargs = {} if numeric_only is lib.no_default else {"numeric_only": numeric_only}

func = getattr(resampled, method)
if numeric_only and numeric_only is not lib.no_default:
    with pytest.raises(TypeError, match="Cannot use numeric_only=True"):
        func(**kwargs)
elif method == "prod":
    with pytest.raises(TypeError, match="can't multiply sequence by non-int"):
        func(**kwargs)
else:
    result = func(**kwargs)
    expected = Series(expected_data, index=expected_index)
    tm.assert_series_equal(result, expected)
