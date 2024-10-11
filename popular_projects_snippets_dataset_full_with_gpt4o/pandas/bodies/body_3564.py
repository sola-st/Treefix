# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
# this is a de-facto sort via unstack
# confirming that we sort in the order of the bins
y = Series(np.random.randn(100))
x1 = Series(np.sign(np.random.randn(100)))
x2 = pd.cut(Series(np.random.randn(100)), bins=[-3, -0.5, 0, 0.5, 3])
model = pd.concat([y, x1, x2], axis=1, keys=["Y", "X1", "X2"])

result = model.groupby(["X1", "X2"], observed=True).mean().unstack()
expected = IntervalIndex.from_tuples(
    [(-3.0, -0.5), (-0.5, 0.0), (0.0, 0.5), (0.5, 3.0)], closed="right"
)
result = result.columns.levels[1].categories
tm.assert_index_equal(result, expected)
