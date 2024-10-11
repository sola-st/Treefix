# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_index.py
# GH 15787
index = MultiIndex.from_product([[1], range(5)], names=["level1", None])
df = DataFrame({"col": range(5)}, index=index, dtype=np.int32)

result = concat([df, df], keys=[1, 2], names=["level2"])
index = MultiIndex.from_product(
    [[1, 2], [1], range(5)], names=["level2", "level1", None]
)
expected = DataFrame({"col": list(range(5)) * 2}, index=index, dtype=np.int32)
tm.assert_frame_equal(result, expected)

result = concat([df, df[:2]], keys=[1, 2], names=["level2"])
level2 = [1] * 5 + [2] * 2
level1 = [1] * 7
no_name = list(range(5)) + list(range(2))
tuples = list(zip(level2, level1, no_name))
index = MultiIndex.from_tuples(tuples, names=["level2", "level1", None])
expected = DataFrame({"col": no_name}, index=index, dtype=np.int32)
tm.assert_frame_equal(result, expected)
