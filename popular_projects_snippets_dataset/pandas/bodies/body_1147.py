# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH 13501
frame = DataFrame(
    np.arange(12).reshape((4, 3)),
    index=[["a", "a", "b", "b"], [1, 2, 1, 2]],
    columns=[["Ohio", "Ohio", "Colorado"], ["Green", "Red", "Green"]],
)
frame.index.names = ["key1", "key2"]
frame.columns.names = ["state", "color"]
with pytest.raises(KeyError, match="\\[2\\] not in index"):
    frame.loc[["b", 2], "Colorado"]
