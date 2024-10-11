# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# make sure that fillna on an empty frame works
df = DataFrame(index=["A", "B", "C"], columns=[1, 2, 3, 4, 5])
result = df.dtypes
expected = Series([np.dtype("object")] * 5, index=[1, 2, 3, 4, 5])
tm.assert_series_equal(result, expected)

result = df.fillna(1)
expected = DataFrame(1, index=["A", "B", "C"], columns=[1, 2, 3, 4, 5])
tm.assert_frame_equal(result, expected)

# empty block
df = DataFrame(index=range(3), columns=["A", "B"], dtype="float64")
result = df.fillna("nan")
expected = DataFrame("nan", index=range(3), columns=["A", "B"])
tm.assert_frame_equal(result, expected)
