# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py

# not currently able to handle duplicate columns
df = pd.DataFrame(np.arange(12).reshape(4, 3), columns=list("aaa")).copy()
msg = "Cannot create parquet dataset with duplicate column names"
self.check_error_on_write(df, fp, ValueError, msg)
