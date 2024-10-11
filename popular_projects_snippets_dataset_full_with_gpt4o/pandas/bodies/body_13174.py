# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
df = pd.DataFrame({"a": pd.timedelta_range("1 day", periods=3)})
if pa_version_under8p0:
    self.check_external_error_on_write(df, pa, NotImplementedError)
else:
    check_round_trip(df, pa)
