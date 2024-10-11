# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py

q = (
    pd.concat([quotes, quotes])
    .sort_values(["time", "ticker"])
    .reset_index(drop=True)
)
result = merge_asof(trades, q, on="time", by="ticker")
expected = self.read_data(datapath, "asof.csv")
tm.assert_frame_equal(result, expected)
