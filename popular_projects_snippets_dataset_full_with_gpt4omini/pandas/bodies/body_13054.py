# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# see gh-11544, gh-12051
df = DataFrame(
    {"col": [1, 2, 3], "date_strings": pd.date_range("2012-01-01", periods=3)}
)
df2 = df.copy()
df2["date_strings"] = df2["date_strings"].dt.strftime("%m/%d/%Y")

with tm.ensure_clean(ext) as pth:
    df2.to_excel(pth)

    res = pd.read_excel(pth, index_col=0)
    tm.assert_frame_equal(df2, res)

    res = pd.read_excel(pth, parse_dates=["date_strings"], index_col=0)
    tm.assert_frame_equal(df, res)

    date_parser = lambda x: datetime.strptime(x, "%m/%d/%Y")
    res = pd.read_excel(
        pth, parse_dates=["date_strings"], date_parser=date_parser, index_col=0
    )
    tm.assert_frame_equal(df, res)
