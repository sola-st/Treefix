# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
raw_dates = Series(date_range("1/1/2001", periods=10))
df = DataFrame(
    {
        "date": raw_dates.map(lambda x: str(x.date())),
        "time": raw_dates.map(lambda x: str(x.time())),
    }
)
res = self.read_html(
    df.to_html(), parse_dates={"datetime": [1, 2]}, index_col=1
)
newdf = DataFrame({"datetime": raw_dates})
tm.assert_frame_equal(newdf, res[0])
