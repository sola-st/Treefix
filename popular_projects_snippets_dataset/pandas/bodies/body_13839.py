# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# like dataframe getitem
subset = box(["A"])

df = DataFrame({"A": [1, 2], "B": [3, 4]}, index=["A", "B"])
expected = IndexSlice[:, ["A"]]

result = non_reducing_slice(subset)
tm.assert_frame_equal(df.loc[result], df.loc[expected])
