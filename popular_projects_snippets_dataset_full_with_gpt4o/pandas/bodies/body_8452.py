# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
start = np.datetime64("1066-10-14")  # Battle of Hastings
end = np.datetime64("2305-07-13")  # Jean-Luc Picard's birthday

dti = date_range(start, end, freq="D", unit="s")
assert dti.freq == "D"
assert dti.dtype == "M8[s]"

exp = np.arange(
    start.astype("M8[s]").view("i8"),
    (end + 1).astype("M8[s]").view("i8"),
    24 * 3600,
).view("M8[s]")

tm.assert_numpy_array_equal(dti.to_numpy(), exp)
