# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH 42790
df = DataFrame(
    [[1, 2], [4, 5], [7, 8]],
    index=["cobra", "viper", "sidewinder"],
    columns=["max_speed", "shield"],
)
expected = df.iloc[:2]
expected.index.name = "foo"
result = df.loc[Index(["cobra", "viper"], name="foo")]
tm.assert_frame_equal(result, expected)
