# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# Regression test on pivot table: no values passed but rows and cols
# are multi-indexed
data["D"] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
result = data[["A", "B", "C", "D"]].pivot_table(
    index=["A", "B"], columns=["C", "D"], aggfunc=len, margins=True
)
assert result.All.tolist() == [3.0, 1.0, 4.0, 3.0, 11.0]
