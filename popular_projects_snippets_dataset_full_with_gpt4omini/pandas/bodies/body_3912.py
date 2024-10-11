# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH 8039
t = datetime(2014, 1, 1)
df = DataFrame([1, 2, 3, 4], columns=MultiIndex.from_tuples([(t, "A", "B")]))
result = df.stack()

eidx = MultiIndex.from_product([(0, 1, 2, 3), ("B",)])
ecols = MultiIndex.from_tuples([(t, "A")])
expected = DataFrame([1, 2, 3, 4], index=eidx, columns=ecols)
tm.assert_frame_equal(result, expected)
