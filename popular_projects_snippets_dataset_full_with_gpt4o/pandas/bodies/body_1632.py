# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#23326
df = DataFrame([list("abc")])
df.loc[:, "col1"] = 5

expected = DataFrame({0: ["a"], 1: ["b"], 2: ["c"], "col1": [5]})
tm.assert_frame_equal(df, expected)
