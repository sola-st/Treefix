# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# Not supported in fastparquet as of 0.1.3 or older pyarrow version
engine = pa

df = pd.DataFrame({"A": [1, 2, 3]})
index = pd.MultiIndex.from_tuples([("a", 1), ("a", 2), ("b", 1)])
df.index = index
check_round_trip(df, engine)
