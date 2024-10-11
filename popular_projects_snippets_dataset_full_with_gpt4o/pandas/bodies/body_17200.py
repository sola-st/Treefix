# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 26568
df = DataFrame([["a", "x", 1], ["a", "y", 2], ["b", "y", 3], ["b", "z", 4]])
df.columns = [10, 20, 30]

result = df.pivot_table(
    index=10, columns=20, values=30, aggfunc="sum", fill_value=0, margins=True
)

expected = DataFrame([[1, 2, 0, 3], [0, 3, 4, 7], [1, 5, 4, 10]])
expected.columns = ["x", "y", "z", "All"]
expected.index = ["a", "b", "All"]
expected.columns.name = 20
expected.index.name = 10

tm.assert_frame_equal(result, expected)
