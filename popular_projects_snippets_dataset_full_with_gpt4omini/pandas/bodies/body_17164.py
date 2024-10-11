# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# Regression test on pivot table: no values passed but rows are a
# multi-index
result = data[["A", "B", "C"]].pivot_table(
    index=["A", "B"], columns="C", aggfunc=len, margins=True
)
assert result.All.tolist() == [3.0, 1.0, 4.0, 3.0, 11.0]
