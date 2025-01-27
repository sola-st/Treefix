# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH16360
result = DataFrame({"A": [1]})
result.loc[:, "B"] = Categorical(["b"], ordered=ordered)
expected = DataFrame({"A": [1], "B": Categorical(["b"], ordered=ordered)})
tm.assert_frame_equal(result, expected)
