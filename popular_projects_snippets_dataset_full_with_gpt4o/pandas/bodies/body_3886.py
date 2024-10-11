# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH 19966
idx = MultiIndex.from_product(
    [["a", "b"], [1, 2], [3, 4]], names=[("A", "a"), "B", "C"]
)
df = DataFrame({"d": [1] * 8, "e": [2] * 8}, index=idx)
result = df.unstack(unstack_idx)

expected = DataFrame(
    expected_values, columns=expected_columns, index=expected_index
)
tm.assert_frame_equal(result, expected)
