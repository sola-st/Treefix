# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# GH 11431
df = DataFrame([[1, 2], [3, 4]], columns=["\xe9", "b"])
df.to_sql("test_unicode", self.conn, index=False)
