# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_series.py
# preserve series names, #2489
s = Series(np.random.randn(5), name="A")
s2 = Series(np.random.randn(5), name="B")

result = concat([s, s2], axis=1)
expected = DataFrame({"A": s, "B": s2})
tm.assert_frame_equal(result, expected)

s2.name = None
result = concat([s, s2], axis=1)
tm.assert_index_equal(result.columns, Index(["A", 0], dtype="object"))
