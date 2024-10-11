# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_convert_dtypes.py
if (
    hasattr(data, "dtype")
    and data.dtype == "M8[ns]"
    and isinstance(maindtype, pd.DatetimeTZDtype)
):
    # this astype is deprecated in favor of tz_localize
    msg = "Cannot use .astype to convert from timezone-naive dtype"
    with pytest.raises(TypeError, match=msg):
        pd.Series(data, dtype=maindtype)
    exit()

if maindtype is not None:
    series = pd.Series(data, dtype=maindtype)
else:
    series = pd.Series(data)

result = series.convert_dtypes(*params)

param_names = [
    "infer_objects",
    "convert_string",
    "convert_integer",
    "convert_boolean",
    "convert_floating",
]
params_dict = dict(zip(param_names, params))

expected_dtype = expected_default
for spec, dtype in expected_other.items():
    if all(params_dict[key] is val for key, val in zip(spec[::2], spec[1::2])):
        expected_dtype = dtype

expected = pd.Series(data, dtype=expected_dtype)
tm.assert_series_equal(result, expected)

# Test that it is a copy
copy = series.copy(deep=True)

result[result.notna()] = np.nan

# Make sure original not changed
tm.assert_series_equal(series, copy)
