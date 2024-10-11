# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
# gh-13613: these should not error because errors='ignore'
invalid_data = "apple"
assert invalid_data == to_timedelta(invalid_data, errors="ignore")

invalid_data = ["apple", "1 days"]
tm.assert_numpy_array_equal(
    np.array(invalid_data, dtype=object),
    to_timedelta(invalid_data, errors="ignore"),
)

invalid_data = pd.Index(["apple", "1 days"])
tm.assert_index_equal(invalid_data, to_timedelta(invalid_data, errors="ignore"))

invalid_data = Series(["apple", "1 days"])
tm.assert_series_equal(
    invalid_data, to_timedelta(invalid_data, errors="ignore")
)
