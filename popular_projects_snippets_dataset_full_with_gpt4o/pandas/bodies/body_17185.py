# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH #18713
# for consistency purposes
data = data.drop(columns="C")
result = pivot_table(data, index="A", columns="B", aggfunc=f)
expected = pivot_table(data, index="A", columns="B", aggfunc=f_numpy)
tm.assert_frame_equal(result, expected)
