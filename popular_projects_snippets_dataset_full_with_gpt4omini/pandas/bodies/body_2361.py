# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
df = four_level_index_dataframe
expected_values = [[0.4473, 1.4152, 0.2834, 1.00661, 0.1744]]
expected_index = MultiIndex(
    levels=[["q"], [20.0]], codes=[[0], [0]], names=["two", "three"]
)
expected = DataFrame(
    expected_values, index=expected_index, columns=list("ABCDE")
)
result = indexer(df)
tm.assert_frame_equal(result, expected)
