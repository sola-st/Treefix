# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
obj = pd.Series([1, 2, 3, 4], index=list("abcd"))
assert obj.index.dtype == object

if exp_dtype is IndexError:
    temp = obj.copy()
    msg = "index 5 is out of bounds for axis 0 with size 4"
    with pytest.raises(exp_dtype, match=msg):
        temp[5] = 5
else:
    exp_index = pd.Index(list("abcd") + [val])
    self._assert_setitem_index_conversion(obj, val, exp_index, exp_dtype)
