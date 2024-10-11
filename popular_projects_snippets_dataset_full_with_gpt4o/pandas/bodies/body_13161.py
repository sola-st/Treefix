# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
engine = pa
dates = pd.date_range("01-Jan-2018", "01-Dec-2018", freq="MS")
df = pd.DataFrame(np.random.randn(2 * len(dates), 3), columns=list("ABC"))
index1 = pd.MultiIndex.from_product(
    [["Level1", "Level2"], dates], names=["level", "date"]
)
index2 = index1.copy(names=None)
for index in [index1, index2]:
    df.index = index

    check_round_trip(df, engine)
    check_round_trip(
        df, engine, read_kwargs={"columns": ["A", "B"]}, expected=df[["A", "B"]]
    )
