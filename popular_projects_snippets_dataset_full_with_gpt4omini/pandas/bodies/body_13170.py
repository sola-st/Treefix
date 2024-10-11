# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py

df = df_full

# additional supported types for pyarrow
dti = pd.date_range("20130101", periods=3, tz="Europe/Brussels")
dti = dti._with_freq(None)  # freq doesn't round-trip
df["datetime_tz"] = dti
df["bool_with_none"] = [True, None, True]

check_round_trip(df, pa)
