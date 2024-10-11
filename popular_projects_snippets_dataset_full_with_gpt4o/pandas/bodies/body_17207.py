# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
df = DataFrame(data=[("A", "1", "A1"), ("B", "2", "B2")])

result = df.pivot(index=1, columns=0, values=2)
repr(result)
tm.assert_index_equal(result.columns, Index(["A", "B"], name=0))
