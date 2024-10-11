# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# GH #27339
df = pd.DataFrame(index=[], columns=[])
check_round_trip(df, pa)
