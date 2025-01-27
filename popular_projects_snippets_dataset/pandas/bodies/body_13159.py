# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
check_names = engine != "fastparquet"

df = pd.DataFrame({"A": [1, 2, 3]})
check_round_trip(df, engine)

indexes = [
    [2, 3, 4],
    pd.date_range("20130101", periods=3),
    list("abc"),
    [1, 3, 4],
]
# non-default index
for index in indexes:
    df.index = index
    if isinstance(index, pd.DatetimeIndex):
        df.index = df.index._with_freq(None)  # freq doesn't round-trip
    check_round_trip(df, engine, check_names=check_names)

# index with meta-data
df.index = [0, 1, 2]
df.index.name = "foo"
check_round_trip(df, engine)
