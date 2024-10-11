# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH#12564

df = DataFrame({"A": ["foo", "bar", "baz"]})
exp = DataFrame({"A": [True, False, False]})

res = df == "foo"
tm.assert_frame_equal(res, exp)

# casting to categorical shouldn't affect the result
df["A"] = df["A"].astype("category")

res = df == "foo"
tm.assert_frame_equal(res, exp)
