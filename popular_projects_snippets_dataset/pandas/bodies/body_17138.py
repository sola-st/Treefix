# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
result = pivot_table(
    data, values=["D", "E"], index="A", columns=["B", "C"], fill_value=0
)
expected = pivot_table(
    data.drop(["F"], axis=1), index="A", columns=["B", "C"], fill_value=0
)
tm.assert_frame_equal(result, expected)
