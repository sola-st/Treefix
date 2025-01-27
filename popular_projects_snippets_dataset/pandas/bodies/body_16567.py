# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py
# GH 25760
# GH 28956

midx1 = MultiIndex.from_product([[1, 2], [3, 4]], names=["a", "b"])
midx3 = MultiIndex.from_tuples([(4, 1), (3, 2), (3, 1)], names=["b", "a"])

left = DataFrame(index=midx1, data={"x": [10, 20, 30, 40]})
right = DataFrame(index=midx3, data={"y": ["foo", "bar", "fing"]})

result = left.join(right)

expected = DataFrame(
    index=midx1,
    data={"x": [10, 20, 30, 40], "y": ["fing", "foo", "bar", np.nan]},
)

tm.assert_frame_equal(result, expected)
