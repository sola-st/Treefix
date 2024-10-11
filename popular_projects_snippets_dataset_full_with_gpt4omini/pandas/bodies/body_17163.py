# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# Regression test on pivot table: no values or cols passed.
result = data[["A", "B"]].pivot_table(
    index=["A", "B"], aggfunc=len, margins=True
)
result_list = result.tolist()
assert sum(result_list[:-1]) == result_list[-1]
