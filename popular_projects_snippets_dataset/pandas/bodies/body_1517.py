# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH6173, various appends to an empty dataframe

data = [1, 2, 3]
expected = DataFrame({"x": data, "y": [None] * len(data)})

# appends to fit length of data
df = DataFrame(columns=["x", "y"])
df.loc[:, "x"] = data
tm.assert_frame_equal(df, expected)
