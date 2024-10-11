# Extracted from ./data/repos/pandas/pandas/tests/extension/base/groupby.py
# GH#41720
expected = pd.DataFrame(
    {
        "td": {
            0: pd.Timedelta("0 days 01:00:00"),
            1: pd.Timedelta("0 days 01:15:00"),
            2: pd.Timedelta("0 days 01:15:00"),
        }
    }
)
df = pd.DataFrame(
    {
        "td": pd.Series(
            ["0 days 01:00:00", "0 days 00:15:00", "0 days 01:15:00"],
            dtype="timedelta64[ns]",
        ),
        "grps": ["a", "a", "b"],
    }
)
gb = df.groupby("grps")
result = gb.agg(td=("td", "cumsum"))
self.assert_frame_equal(result, expected)
