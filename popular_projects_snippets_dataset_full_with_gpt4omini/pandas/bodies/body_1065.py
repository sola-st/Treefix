# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_getitem.py
# selecting a non_unique from the 2nd level
df = dataframe_with_duplicate_index
expected = DataFrame(
    [["d", 4, 4], ["e", 5, 5]],
    index=Index(["B2", "B2"], name="sub"),
    columns=["h1", "h3", "h5"],
).T
result = df["A"]["B2"]
tm.assert_frame_equal(result, expected)
