# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
df = pd.DataFrame({"a": [True, None, False]})
expected = pd.DataFrame({"a": [1.0, np.nan, 0.0]}, dtype="float16")
# Fastparquet bug in 0.7.1 makes it so that this dtype becomes
# float64
check_round_trip(df, fp, expected=expected, check_dtype=False)
