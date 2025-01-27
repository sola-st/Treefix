# Extracted from ./data/repos/pandas/pandas/tests/strings/test_string_array.py
method_name, args, kwargs = any_string_method

data = ["a", "bb", np.nan, "ccc"]
a = Series(data, dtype=object)
b = Series(data, dtype=nullable_string_dtype)

if method_name == "decode":
    with pytest.raises(TypeError, match="a bytes-like object is required"):
        getattr(b.str, method_name)(*args, **kwargs)
    exit()

expected = getattr(a.str, method_name)(*args, **kwargs)
result = getattr(b.str, method_name)(*args, **kwargs)

if isinstance(expected, Series):
    if expected.dtype == "object" and lib.is_string_array(
        expected.dropna().values,
    ):
        assert result.dtype == nullable_string_dtype
        result = result.astype(object)

    elif expected.dtype == "object" and lib.is_bool_array(
        expected.values, skipna=True
    ):
        assert result.dtype == "boolean"
        result = result.astype(object)

    elif expected.dtype == "bool":
        assert result.dtype == "boolean"
        result = result.astype("bool")

    elif expected.dtype == "float" and expected.isna().any():
        assert result.dtype == "Int64"
        result = result.astype("float")

elif isinstance(expected, DataFrame):
    columns = expected.select_dtypes(include="object").columns
    assert all(result[columns].dtypes == nullable_string_dtype)
    result[columns] = result[columns].astype(object)
tm.assert_equal(result, expected)
