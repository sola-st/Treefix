# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_timedelta.py

# doc example

scalar = Timedelta(days=31)
td = index_or_series(
    [scalar, scalar, scalar + timedelta(minutes=5, seconds=3), NaT],
    dtype="m8[ns]",
)

result = td / np.timedelta64(1, "D")
expected = index_or_series(
    [31, 31, (31 * 86400 + 5 * 60 + 3) / 86400.0, np.nan]
)
tm.assert_equal(result, expected)

# We don't support "D" reso, so we use the pre-2.0 behavior
#  casting to float64
msg = (
    r"Cannot convert from timedelta64\[ns\] to timedelta64\[D\]. "
    "Supported resolutions are 's', 'ms', 'us', 'ns'"
)
with pytest.raises(ValueError, match=msg):
    td.astype("timedelta64[D]")

result = td / np.timedelta64(1, "s")
expected = index_or_series(
    [31 * 86400, 31 * 86400, 31 * 86400 + 5 * 60 + 3, np.nan]
)
tm.assert_equal(result, expected)

exp_values = np.asarray(td).astype("m8[s]")
exp_tda = TimedeltaArray._simple_new(exp_values, dtype=exp_values.dtype)
expected = index_or_series(exp_tda)
assert expected.dtype == "m8[s]"
result = td.astype("timedelta64[s]")
tm.assert_equal(result, expected)
