# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
gb = df.groupby("group")

# object dtypes for transformations are not implemented in Cython and
# have no Python fallback
exception = NotImplementedError if method.startswith("cum") else TypeError

if method in ("min", "max", "cummin", "cummax", "cumsum", "cumprod"):
    # The methods default to numeric_only=False and raise TypeError
    msg = "|".join(
        [
            "Categorical is not ordered",
            "function is not implemented for this dtype",
        ]
    )
    with pytest.raises(exception, match=msg):
        getattr(gb, method)()
elif method in ("sum", "mean", "median", "prod"):
    msg = "|".join(
        [
            "category type does not support sum operations",
            "[Cc]ould not convert",
            "can't multiply sequence by non-int of type 'str'",
        ]
    )
    with pytest.raises(exception, match=msg):
        getattr(gb, method)()
else:
    result = getattr(gb, method)()
    tm.assert_index_equal(result.columns, expected_columns_numeric)

if method not in ("first", "last"):
    msg = "|".join(
        [
            "[Cc]ould not convert",
            "Categorical is not ordered",
            "category type does not support",
            "can't multiply sequence",
            "function is not implemented for this dtype",
        ]
    )
    with pytest.raises(exception, match=msg):
        getattr(gb, method)(numeric_only=False)
else:
    result = getattr(gb, method)(numeric_only=False)
    tm.assert_index_equal(result.columns, expected_columns)
