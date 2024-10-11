# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH#15928
path = datapath("reshape", "merge", "data", "quotes2.csv")
df = pd.read_csv(path, parse_dates=["time"])
df2 = df.set_index(["ticker", "time"]).sort_index()

res = df2.loc[("AAPL", slice("2016-05-25 13:30:00")), :].droplevel(0)
expected = df2.loc["AAPL"].loc[slice("2016-05-25 13:30:00"), :]
tm.assert_frame_equal(res, expected)
