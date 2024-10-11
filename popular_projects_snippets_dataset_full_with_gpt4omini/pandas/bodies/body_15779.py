# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# see GH#7271
ser = Series(range(0, 10, 2), name="abc")

dt1 = dtype_class({"abc": str})
result = ser.astype(dt1)
expected = Series(["0", "2", "4", "6", "8"], name="abc")
tm.assert_series_equal(result, expected)

dt2 = dtype_class({"abc": "float64"})
result = ser.astype(dt2)
expected = Series([0.0, 2.0, 4.0, 6.0, 8.0], dtype="float64", name="abc")
tm.assert_series_equal(result, expected)

dt3 = dtype_class({"abc": str, "def": str})
msg = (
    "Only the Series name can be used for the key in Series dtype "
    r"mappings\."
)
with pytest.raises(KeyError, match=msg):
    ser.astype(dt3)

dt4 = dtype_class({0: str})
with pytest.raises(KeyError, match=msg):
    ser.astype(dt4)

# GH#16717
# if dtypes provided is empty, it should error
if dtype_class is Series:
    dt5 = dtype_class({}, dtype=object)
else:
    dt5 = dtype_class({})

with pytest.raises(KeyError, match=msg):
    ser.astype(dt5)
