# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py

# GH 23070
float_data = [1, np.nan, 3, np.nan]
datetime_data = [
    Timestamp("1960-02-15"),
    Timestamp("1960-02-16"),
    pd.NaT,
    pd.NaT,
]
df = DataFrame({"A": float_data, "B": datetime_data})

result = df.any(axis=1)
expected = Series([True, True, True, False])
tm.assert_series_equal(result, expected)
