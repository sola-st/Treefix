# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# see gh-24910
kwargs = {"errors": errors} if errors is not None else {}
val = -large_val if signed else large_val
val = transform(val)

extra_elt = "string"
arr = [val] + multiple_elts * [extra_elt]

val_is_string = isinstance(val, str)
coercing = errors == "coerce"

if errors in (None, "raise") and (val_is_string or multiple_elts):
    if val_is_string:
        msg = "Integer out of range. at position 0"
    else:
        msg = 'Unable to parse string "string" at position 1'

    with pytest.raises(ValueError, match=msg):
        to_numeric(arr, **kwargs)
else:
    result = to_numeric(arr, **kwargs)

    exp_val = float(val) if (coercing and val_is_string) else val
    expected = [exp_val]

    if multiple_elts:
        if coercing:
            expected.append(np.nan)
            exp_dtype = float
        else:
            expected.append(extra_elt)
            exp_dtype = object
    else:
        exp_dtype = float if isinstance(exp_val, (int, float)) else object

    tm.assert_almost_equal(result, np.array(expected, dtype=exp_dtype))
