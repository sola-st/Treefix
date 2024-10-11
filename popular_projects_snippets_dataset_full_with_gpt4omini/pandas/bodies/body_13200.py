# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py

# period
df = pd.DataFrame({"a": pd.period_range("2013", freq="M", periods=3)})
# error from fastparquet -> don't check exact error message
self.check_error_on_write(df, fp, ValueError, None)

# mixed
df = pd.DataFrame({"a": ["a", 1, 2.0]})
msg = "Can't infer object conversion type"
self.check_error_on_write(df, fp, ValueError, msg)
