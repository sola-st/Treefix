# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
df = pd.DataFrame({"string": list("abc"), "int": list(range(1, 4))})

# unicode
df.columns = ["foo", "bar"]
check_round_trip(df, engine)
