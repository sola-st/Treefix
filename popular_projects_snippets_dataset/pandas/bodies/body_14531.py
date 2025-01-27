# Extracted from ./data/repos/pandas/pandas/tests/io/test_feather.py
df = tm.makeDataFrame().reset_index()
self.check_round_trip(df, write_kwargs={"version": 1})
