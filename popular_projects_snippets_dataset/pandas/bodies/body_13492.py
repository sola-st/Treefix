# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
df = DataFrame({"From": np.ones(5)})
assert sql.to_sql(df, con=sqlite_buildin, name="testkeywords", index=False) == 5
