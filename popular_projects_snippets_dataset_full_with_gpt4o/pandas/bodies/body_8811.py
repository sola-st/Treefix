# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
# GH 37987

arr = pd.array(["a", pd.NA], dtype=dtype)

res = arr.fillna(value="b")
expected = pd.array(["a", "b"], dtype=dtype)
tm.assert_extension_array_equal(res, expected)

res = arr.fillna(value=np.str_("b"))
expected = pd.array(["a", "b"], dtype=dtype)
tm.assert_extension_array_equal(res, expected)

if dtype.storage == "pyarrow":
    err = TypeError
    msg = "Invalid value '1' for dtype string"
else:
    err = ValueError
    msg = "Cannot set non-string value '1' into a StringArray."
with pytest.raises(err, match=msg):
    arr.fillna(value=1)
