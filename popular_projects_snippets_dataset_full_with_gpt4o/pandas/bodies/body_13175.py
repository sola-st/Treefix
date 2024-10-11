# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# mixed python objects
df = pd.DataFrame({"a": ["a", 1, 2.0]})
# pyarrow 0.11 raises ArrowTypeError
# older pyarrows raise ArrowInvalid
self.check_external_error_on_write(df, pa, pyarrow.ArrowException)
