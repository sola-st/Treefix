# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# GH 9736
df = DataFrame(np.random.randn(2, 2))
mask = DataFrame([[False, False], [False, False]])
ser = Series([0, 1])

expected = DataFrame([[0, 0], [1, 1]], dtype="float64")
result = df.where(mask, ser, axis="index")
tm.assert_frame_equal(result, expected)

result = df.copy()
return_value = result.where(mask, ser, axis="index", inplace=True)
assert return_value is None
tm.assert_frame_equal(result, expected)

expected = DataFrame([[0, 1], [0, 1]], dtype="float64")
result = df.where(mask, ser, axis="columns")
tm.assert_frame_equal(result, expected)

result = df.copy()
return_value = result.where(mask, ser, axis="columns", inplace=True)
assert return_value is None
tm.assert_frame_equal(result, expected)
