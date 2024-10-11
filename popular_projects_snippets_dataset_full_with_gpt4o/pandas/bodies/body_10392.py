# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# GH 15429
# transforming a datetime to timedelta
df = DataFrame({"A": Timestamp("20130101"), "B": np.arange(5)})
expected = Series([Timestamp("20130101") - Timestamp("20130101")] * 5, name="A")

# this does date math without changing result type in transform
base_time = df["A"][0]
result = (
    df.groupby("A")["A"].transform(lambda x: x.max() - x.min() + base_time)
    - base_time
)
tm.assert_series_equal(result, expected)

# this does date math and causes the transform to return timedelta
result = df.groupby("A")["A"].transform(lambda x: x.max() - x.min())
tm.assert_series_equal(result, expected)
