# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
# axis=0
df = DataFrame(np.random.randn(3, 4))
df2 = DataFrame(np.random.randn(4, 4))

result = concat([df, df2], keys=[0, 1])
exp_index = MultiIndex.from_arrays(
    [[0, 0, 0, 1, 1, 1, 1], [0, 1, 2, 0, 1, 2, 3]]
)
expected = DataFrame(np.r_[df.values, df2.values], index=exp_index)
tm.assert_frame_equal(result, expected)

result = concat([df, df], keys=[0, 1])
exp_index2 = MultiIndex.from_arrays([[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]])
expected = DataFrame(np.r_[df.values, df.values], index=exp_index2)
tm.assert_frame_equal(result, expected)

# axis=1
df = DataFrame(np.random.randn(4, 3))
df2 = DataFrame(np.random.randn(4, 4))

result = concat([df, df2], keys=[0, 1], axis=1)
expected = DataFrame(np.c_[df.values, df2.values], columns=exp_index)
tm.assert_frame_equal(result, expected)

result = concat([df, df], keys=[0, 1], axis=1)
expected = DataFrame(np.c_[df.values, df.values], columns=exp_index2)
tm.assert_frame_equal(result, expected)
