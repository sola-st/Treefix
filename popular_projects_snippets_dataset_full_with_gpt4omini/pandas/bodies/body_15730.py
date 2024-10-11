# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_to_csv.py
# GH 28210
s = Series(["foo", "bar", "baz"], index=pd.interval_range(0, 3))

with tm.ensure_clean("__tmp_to_csv_interval_index__.csv") as path:
    s.to_csv(path, header=False)
    result = self.read_csv(path, index_col=0)

    # can't roundtrip intervalindex via read_csv so check string repr (GH 23595)
    expected = s.copy()
    expected.index = expected.index.astype(str)

    tm.assert_series_equal(result, expected)
