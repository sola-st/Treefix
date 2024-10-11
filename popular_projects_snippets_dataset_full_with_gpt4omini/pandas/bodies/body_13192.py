# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# with version 2.6, pyarrow defaults to writing the nanoseconds, so
# this should work without error
# Note in previous pyarrows(<6.0.0), only the pseudo-version 2.0 was available
if not pa_version_under6p0:
    ver = "2.6"
else:
    ver = "2.0"
df = pd.DataFrame({"a": pd.date_range("2017-01-01", freq="1n", periods=10)})
check_round_trip(df, pa, write_kwargs={"version": ver})
