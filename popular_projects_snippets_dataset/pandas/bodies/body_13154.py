# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
for obj in [
    pd.Series([1, 2, 3]),
    1,
    "foo",
    pd.Timestamp("20130101"),
    np.array([1, 2, 3]),
]:
    msg = "to_parquet only supports IO with DataFrames"
    self.check_error_on_write(obj, engine, ValueError, msg)
