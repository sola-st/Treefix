# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
idx1 = pd.DatetimeIndex(
    ["2013-04-01 9:00", "2013-04-02 9:00", "2013-04-03 9:00"] * 2, tz="Asia/Tokyo"
)
idx2 = date_range("2010/01/01", periods=6, freq="M", tz="US/Eastern")
idx = MultiIndex.from_arrays([idx1, idx2])

expected1 = pd.DatetimeIndex(
    ["2013-04-01 9:00", "2013-04-02 9:00", "2013-04-03 9:00"], tz="Asia/Tokyo"
)

tm.assert_index_equal(idx.levels[0], expected1)
tm.assert_index_equal(idx.levels[1], idx2)

# from datetime combos
# GH 7888
date1 = np.datetime64("today")
date2 = datetime.today()
date3 = Timestamp.today()

for d1, d2 in itertools.product([date1, date2, date3], [date1, date2, date3]):
    index = MultiIndex.from_product([[d1], [d2]])
    assert isinstance(index.levels[0], pd.DatetimeIndex)
    assert isinstance(index.levels[1], pd.DatetimeIndex)

# but NOT date objects, matching Index behavior
date4 = date.today()
index = MultiIndex.from_product([[date4], [date2]])
assert not isinstance(index.levels[0], pd.DatetimeIndex)
assert isinstance(index.levels[1], pd.DatetimeIndex)
