# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop_duplicates.py
# GH17836
df = DataFrame([[1, 2, 5], [3, 4, 6], [3, 4, 7]], columns=["a", "a", "b"])

result0 = df.drop_duplicates()
tm.assert_frame_equal(result0, df)

result1 = df.drop_duplicates("a")
expected1 = df[:2]
tm.assert_frame_equal(result1, expected1)
