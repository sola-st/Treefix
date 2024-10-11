# Extracted from ./data/repos/pandas/pandas/tests/io/test_feather.py

# mixed python objects
df = pd.DataFrame({"a": ["a", 1, 2.0]})
self.check_external_error_on_write(df)
