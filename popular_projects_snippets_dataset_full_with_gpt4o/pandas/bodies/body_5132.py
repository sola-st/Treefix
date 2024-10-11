# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#18846
td = Timedelta(hours=3, minutes=4)

msg = "|".join(
    [
        r"Invalid dtype datetime64\[D\] for __floordiv__",
        "'dtype' is an invalid keyword argument for this function",
        r"ufunc '?floor_divide'? cannot use operands with types",
    ]
)
with pytest.raises(TypeError, match=msg):
    td // np.datetime64("2016-01-01", dtype="datetime64[us]")
