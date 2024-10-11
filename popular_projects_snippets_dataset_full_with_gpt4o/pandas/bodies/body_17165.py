# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# Regression test on pivot table: no values passed but row and col
# defined
result = data[["A", "B"]].pivot_table(
    index="A", columns="B", aggfunc=len, margins=True
)
assert result.All.tolist() == [4.0, 7.0, 11.0]
