# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
# see gh-3062
parser = all_parsers
df = DataFrame(
    dict({"A": np.arange(10, dtype="float64"), "B": Timestamp("20010101")})
)
df.iloc[3:6, :] = np.nan

with tm.ensure_clean("__nat_parse_.csv") as path:
    df.to_csv(path)

    result = parser.read_csv(path, index_col=0, parse_dates=["B"])
    tm.assert_frame_equal(result, df)
