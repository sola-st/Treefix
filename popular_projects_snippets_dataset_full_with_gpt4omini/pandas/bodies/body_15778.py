# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# see GH#14878
ser = Series([1, 2, 3])

msg = (
    r"Expected value of kwarg 'errors' to be one of \['raise', "
    r"'ignore'\]\. Supplied value is 'False'"
)
with pytest.raises(ValueError, match=msg):
    ser.astype(np.float64, errors=False)

ser.astype(np.int8, errors="raise")
