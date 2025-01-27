# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_values.py
tz = "US/Central"
df = DataFrame({"A": date_range("2000", periods=4, tz=tz)})
result = df.values
expected = np.array(
    [
        [Timestamp("2000-01-01", tz=tz)],
        [Timestamp("2000-01-02", tz=tz)],
        [Timestamp("2000-01-03", tz=tz)],
        [Timestamp("2000-01-04", tz=tz)],
    ]
)
tm.assert_numpy_array_equal(result, expected)

# two columns, homogeneous

df["B"] = df["A"]
result = df.values
expected = np.concatenate([expected, expected], axis=1)
tm.assert_numpy_array_equal(result, expected)

# three columns, heterogeneous
est = "US/Eastern"
df["C"] = df["A"].dt.tz_convert(est)

new = np.array(
    [
        [Timestamp("2000-01-01T01:00:00", tz=est)],
        [Timestamp("2000-01-02T01:00:00", tz=est)],
        [Timestamp("2000-01-03T01:00:00", tz=est)],
        [Timestamp("2000-01-04T01:00:00", tz=est)],
    ]
)
expected = np.concatenate([expected, new], axis=1)
result = df.values
tm.assert_numpy_array_equal(result, expected)
