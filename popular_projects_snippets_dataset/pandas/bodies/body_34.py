# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_transform.py
# GH 35964
obj = unpack_obj(float_frame, frame_or_series, axis)

with np.errstate(all="ignore"):
    f_sqrt = np.sqrt(obj)

# ufunc
result = obj.transform(np.sqrt, axis=axis)
expected = f_sqrt
tm.assert_equal(result, expected)
