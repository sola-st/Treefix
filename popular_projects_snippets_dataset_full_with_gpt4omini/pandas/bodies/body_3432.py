# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
# GH#45230
df = DataFrame(
    columns=["brand"], dtype=np.int64, index=RangeIndex(0, 0, 1, name="foo")
)

df2 = df.set_index([df.index, "brand"])

result = df2.reset_index([1], drop=True)
tm.assert_frame_equal(result, df[[]], check_index_type=True)
