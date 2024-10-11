# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# GH 20653
df = DataFrame(
    [["foo", True], [np.nan, True], ["foo", True]], columns=["key", "val"]
)

exp = Series([True, np.nan, True], name="val")

res = df.groupby("key")["val"].transform(func)
tm.assert_series_equal(res, exp)
