# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py

expected = self.read_data(datapath, "asof2.csv")
trades = self.read_data(datapath, "trades2.csv")
quotes = self.read_data(datapath, "quotes2.csv", dedupe=True)

result = merge_asof(trades, quotes, on="time", by="ticker")
tm.assert_frame_equal(result, expected)
