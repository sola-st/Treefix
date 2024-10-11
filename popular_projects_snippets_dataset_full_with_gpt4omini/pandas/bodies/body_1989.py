# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# see gh-24910
kwargs = {"errors": errors} if errors is not None else {}
val = -large_val if signed else large_val

val = transform(val)
val_is_string = isinstance(val, str)

if val_is_string and errors in (None, "raise"):
    msg = "Integer out of range. at position 0"
    with pytest.raises(ValueError, match=msg):
        to_numeric(val, **kwargs)
else:
    expected = float(val) if (errors == "coerce" and val_is_string) else val
    tm.assert_almost_equal(to_numeric(val, **kwargs), expected)
