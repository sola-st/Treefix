# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_duplicates.py
idx1 = DatetimeIndex(
    ["2015-01-01", "2015-01-01", "2015-01-01", "2015-01-01", "NaT", "NaT"]
)
idx2 = DatetimeIndex(
    ["2015-01-01", "2015-01-01", "2015-01-02", "2015-01-02", "NaT", "2015-01-01"],
    tz="Asia/Tokyo",
)
result = MultiIndex.from_arrays([idx1, idx2]).unique()

eidx1 = DatetimeIndex(["2015-01-01", "2015-01-01", "NaT", "NaT"])
eidx2 = DatetimeIndex(
    ["2015-01-01", "2015-01-02", "NaT", "2015-01-01"], tz="Asia/Tokyo"
)
exp = MultiIndex.from_arrays([eidx1, eidx2])
tm.assert_index_equal(result, exp)
