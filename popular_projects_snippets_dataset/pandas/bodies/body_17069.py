# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_index.py
# GitHub #44786
df = DataFrame({"col": ["a", "b", "c"]}, index=["1", "2", "2"])
df = concat([df], keys=["X"])

iterables = [["X"], ["1", "2", "2"]]
result_index = df.index
expected_index = MultiIndex.from_product(iterables)

tm.assert_index_equal(result_index, expected_index)

result_df = df
expected_df = DataFrame(
    {"col": ["a", "b", "c"]}, index=MultiIndex.from_product(iterables)
)
tm.assert_frame_equal(result_df, expected_df)
