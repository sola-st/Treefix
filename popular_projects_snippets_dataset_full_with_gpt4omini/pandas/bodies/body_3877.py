# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH 18310
levels = [range(3), [3, "a", "b"], [1, 2]]

# flat columns:
df = DataFrame(1, index=levels[0], columns=levels[1])
result = df.stack()
expected = Series(1, index=MultiIndex.from_product(levels[:2]))
tm.assert_series_equal(result, expected)

# MultiIndex columns:
df = DataFrame(1, index=levels[0], columns=MultiIndex.from_product(levels[1:]))
result = df.stack(1)
expected = DataFrame(
    1, index=MultiIndex.from_product([levels[0], levels[2]]), columns=levels[1]
)
tm.assert_frame_equal(result, expected)

# as above, but used labels in level are actually of homogeneous type
result = df[["a", "b"]].stack(1)
expected = expected[["a", "b"]]
tm.assert_frame_equal(result, expected)
