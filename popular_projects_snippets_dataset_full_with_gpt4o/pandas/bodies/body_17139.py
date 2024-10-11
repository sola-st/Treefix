# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
f = lambda func: pivot_table(
    data, values=["D", "E"], index=["A", "B"], columns="C", aggfunc=func
)
result = f([np.mean, np.std])
means = f(np.mean)
stds = f(np.std)
expected = concat([means, stds], keys=["mean", "std"], axis=1)
tm.assert_frame_equal(result, expected)

# margins not supported??
f = lambda func: pivot_table(
    data,
    values=["D", "E"],
    index=["A", "B"],
    columns="C",
    aggfunc=func,
    margins=True,
)
result = f([np.mean, np.std])
means = f(np.mean)
stds = f(np.std)
expected = concat([means, stds], keys=["mean", "std"], axis=1)
tm.assert_frame_equal(result, expected)
