# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
df = df_full

dti = pd.date_range("20130101", periods=3, tz="US/Eastern")
dti = dti._with_freq(None)  # freq doesn't round-trip
df["datetime_tz"] = dti
df["timedelta"] = pd.timedelta_range("1 day", periods=3)
check_round_trip(df, fp)
