# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH10417
df = DataFrame(
    np.arange(12).reshape(4, 3),
    index=idx,
    columns=columns,
)
result = df.stack()
expected = Series(np.arange(12), index=exp_idx)
tm.assert_series_equal(result, expected)
assert result.index.is_unique is False
li, ri = result.index, expected.index
tm.assert_index_equal(li, ri)
