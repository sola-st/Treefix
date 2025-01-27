# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# GH18628

df = df_full
# additional supported types for pyarrow
df["datetime_tz"] = pd.date_range("20130101", periods=3, tz="Europe/Brussels")

check_round_trip(
    df,
    pa,
    expected=df[["string", "int"]],
    read_kwargs={"columns": ["string", "int"]},
)
