# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# https://github.com/pandas-dev/pandas/issues/41797
df = DataFrame(["a", "b", np.nan])
expected = df.astype(str)
cat = df.astype("category")
result = cat.astype(str)
tm.assert_frame_equal(result, expected)
