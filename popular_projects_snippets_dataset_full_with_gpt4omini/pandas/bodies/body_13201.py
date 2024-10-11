# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
df = pd.DataFrame({"a": pd.Categorical(list("abc"))})
check_round_trip(df, fp)
