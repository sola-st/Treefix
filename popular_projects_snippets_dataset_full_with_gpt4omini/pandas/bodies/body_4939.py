# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py

# GH#7869
# consistency on empty

# float
result = getattr(Series(dtype=float), method)()
assert isna(result)

# timedelta64[ns]
tdser = Series([], dtype="m8[ns]")
if method == "var":
    msg = "|".join(
        [
            "operation 'var' not allowed",
            r"cannot perform var with type timedelta64\[ns\]",
            "does not support reduction 'var'",
        ]
    )
    with pytest.raises(TypeError, match=msg):
        getattr(tdser, method)()
else:
    result = getattr(tdser, method)()
    assert result is NaT
