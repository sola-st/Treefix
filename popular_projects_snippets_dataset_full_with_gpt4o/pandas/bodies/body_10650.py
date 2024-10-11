# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_min_max.py
# GH26321
dates = pd.to_datetime(
    Series(["2019-05-09", "2019-05-09", "2019-05-09"]), format="%Y-%m-%d"
).dt.date
df = DataFrame({"a": [np.nan, "1", np.nan], "b": [0, 1, 1], "c": dates})

result = df.groupby("b", as_index=False)["c"].min()["c"]
expected = pd.to_datetime(
    Series(["2019-05-09", "2019-05-09"], name="c"), format="%Y-%m-%d"
).dt.date
tm.assert_series_equal(result, expected)

result = df.groupby("b")["c"].min()
expected.index.name = "b"
tm.assert_series_equal(result, expected)
