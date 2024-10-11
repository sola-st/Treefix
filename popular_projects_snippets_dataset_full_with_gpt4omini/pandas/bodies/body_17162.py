# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
f = {"D": ["std"], "E": ["sum"]}
expected = data.groupby(["A", "B"]).agg(f).unstack("B")
result = data.pivot_table(index="A", columns="B", aggfunc=f)

tm.assert_frame_equal(result, expected)
