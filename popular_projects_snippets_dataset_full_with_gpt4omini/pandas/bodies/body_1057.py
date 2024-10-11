# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_getitem.py
df = DataFrame({"a": ["1", "2", "3"], "b": ["2", "3", "4"]})
df.columns = [
    ["level1 item1", "level1 item2"],
    ["", "level2 item2"],
    ["level3 item1", "level3 item2"],
]

result = df["level1 item1"]
expected = DataFrame(
    [["1"], ["2"], ["3"]], index=df.index, columns=["level3 item1"]
)
tm.assert_frame_equal(result, expected)
