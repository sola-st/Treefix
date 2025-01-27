# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
df = four_level_index_dataframe
expected_values = [
    [-0.5109, -2.3358, -0.4645, 0.05076, 0.364],
    [0.4473, 1.4152, 0.2834, 1.00661, 0.1744],
]
expected_index = MultiIndex(
    levels=[["b", "q"], [10.0032, 20.0], [4, 5]],
    codes=[[0, 1], [0, 1], [1, 0]],
    names=["two", "three", "four"],
)
expected = DataFrame(
    expected_values, index=expected_index, columns=list("ABCDE")
)

result = indexer(df)
tm.assert_frame_equal(result, expected)
