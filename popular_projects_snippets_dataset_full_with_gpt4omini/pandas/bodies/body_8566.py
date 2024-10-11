# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py

# passing a dtype with a tz should localize
idx = DatetimeIndex(
    ["2013-01-01", "2013-01-02"], dtype="datetime64[ns, US/Eastern]"
)
expected = DatetimeIndex(["2013-01-01", "2013-01-02"]).tz_localize("US/Eastern")
tm.assert_index_equal(idx, expected)

idx = DatetimeIndex(["2013-01-01", "2013-01-02"], tz="US/Eastern")
tm.assert_index_equal(idx, expected)
