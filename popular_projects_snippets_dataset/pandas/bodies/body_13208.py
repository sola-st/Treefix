# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# GH #27339
df = pd.DataFrame(index=[], columns=[])
expected = df.copy()
expected.index.name = "index"
check_round_trip(df, fp, expected=expected)
