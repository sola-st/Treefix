# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_filters.py
df = DataFrame([1, 3, 20, 5, 22, 24, 7])
expected_odd = DataFrame([1, 3, 5, 7], index=[0, 1, 3, 6])
expected_even = DataFrame([20, 22, 24], index=[2, 4, 5])
grouper = df[0].apply(lambda x: x % 2)
grouped = df.groupby(grouper)
tm.assert_frame_equal(grouped.filter(lambda x: x.mean() < 10), expected_odd)
tm.assert_frame_equal(grouped.filter(lambda x: x.mean() > 10), expected_even)
# Test dropna=False.
tm.assert_frame_equal(
    grouped.filter(lambda x: x.mean() < 10, dropna=False),
    expected_odd.reindex(df.index),
)
tm.assert_frame_equal(
    grouped.filter(lambda x: x.mean() > 10, dropna=False),
    expected_even.reindex(df.index),
)
