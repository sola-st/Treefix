# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# tests all units from numeric origination
# GH#19223 / GH#12425
dtype = f"{dtype}[{unit}]"
arr = np.array([[1, 2, 3]], dtype=arr_dtype)
df = DataFrame(arr)
result = df.astype(dtype)
expected = DataFrame(arr.astype(dtype))

tm.assert_frame_equal(result, expected)
