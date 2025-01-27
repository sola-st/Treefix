# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_astype.py
# test astype string with tz and name
dti = date_range("2012-01-01", periods=3, name="test_name", tz="US/Eastern")
result = dti.astype(str)
expected = Index(
    [
        "2012-01-01 00:00:00-05:00",
        "2012-01-02 00:00:00-05:00",
        "2012-01-03 00:00:00-05:00",
    ],
    name="test_name",
    dtype=object,
)
tm.assert_index_equal(result, expected)
