# Extracted from ./data/repos/pandas/pandas/tests/io/test_feather.py

# https://github.com/wesm/feather/issues/53
# not currently able to handle duplicate columns
df = pd.DataFrame(np.arange(12).reshape(4, 3), columns=list("aaa")).copy()
self.check_external_error_on_write(df)
