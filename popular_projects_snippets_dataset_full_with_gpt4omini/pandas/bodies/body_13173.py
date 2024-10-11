# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# not currently able to handle duplicate columns
df = pd.DataFrame(np.arange(12).reshape(4, 3), columns=list("aaa")).copy()
self.check_error_on_write(df, pa, ValueError, "Duplicate column names found")
