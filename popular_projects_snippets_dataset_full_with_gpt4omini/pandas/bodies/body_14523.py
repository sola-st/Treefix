# Extracted from ./data/repos/pandas/pandas/tests/io/test_feather.py

df = pd.DataFrame(np.arange(12).reshape(4, 3)).copy()
msg = "feather must have string column names"
self.check_error_on_write(df, ValueError, msg)
