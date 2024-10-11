# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py

pytest.importorskip("scipy.interpolate")

# GH 16361
df = {"a": [1, 3, 1, 4]}
df = DataFrame(df, index=date_range("2017-01-01", "2017-01-04").as_unit(unit))

expected = df.astype("float64").resample("H").mean()["a"].interpolate("cubic")

result = df.resample("H")["a"].mean().interpolate("cubic")
tm.assert_series_equal(result, expected)

result = df.resample("H").mean()["a"].interpolate("cubic")
tm.assert_series_equal(result, expected)
