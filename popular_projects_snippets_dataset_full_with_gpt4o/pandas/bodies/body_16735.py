# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 9426

right = DataFrame(
    {
        "c": {0: "a", 1: "b", 2: "c", 3: "d", 4: "e"},
        "d": {0: "null", 1: "null", 2: "null", 3: "null", 4: "null"},
    }
)
left = DataFrame(
    {
        "a": {0: "f", 1: "f", 2: "f", 3: "f", 4: "f"},
        "b": {0: "g", 1: "g", 2: "g", 3: "g", 4: "g"},
    }
)
df = merge(left, right, how="left", left_on="b", right_on="c")

# object-object
expected = df.copy()

# object-cat
# note that we propagate the category
# because we don't have any matching rows
cright = right.copy()
cright["d"] = cright["d"].astype("category")
result = merge(left, cright, how="left", left_on="b", right_on="c")
expected["d"] = expected["d"].astype(CategoricalDtype(["null"]))
tm.assert_frame_equal(result, expected)

# cat-object
cleft = left.copy()
cleft["b"] = cleft["b"].astype("category")
result = merge(cleft, cright, how="left", left_on="b", right_on="c")
tm.assert_frame_equal(result, expected)

# cat-cat
cright = right.copy()
cright["d"] = cright["d"].astype("category")
cleft = left.copy()
cleft["b"] = cleft["b"].astype("category")
result = merge(cleft, cright, how="left", left_on="b", right_on="c")
tm.assert_frame_equal(result, expected)
