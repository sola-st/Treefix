# Extracted from ./data/repos/pandas/pandas/tests/base/test_constructors.py
# GH-26853 (+ bug GH-26206 out of bound non-ns unit)

# No dtype specified (dtype inference)
# datetime64[non-ns] raise error, other cases result in object dtype
# and preserve original data
if a.dtype.kind == "M":
    # Can't fit in nanosecond bounds -> get the nearest supported unit
    result = constructor(a)
    assert result.dtype == "M8[s]"
else:
    result = constructor(a)
    assert result.dtype == "object"
    tm.assert_numpy_array_equal(result.to_numpy(), a)

# Explicit dtype specified
# Forced conversion fails for all -> all cases raise error
msg = "Out of bounds|Out of bounds .* present at position 0"
with pytest.raises(pd.errors.OutOfBoundsDatetime, match=msg):
    constructor(a, dtype="datetime64[ns]")
