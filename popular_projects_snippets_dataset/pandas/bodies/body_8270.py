# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_astype.py
# test astype string with freqH and timezone
dti = date_range(
    "3/6/2012 00:00", periods=2, freq="H", tz="Europe/London", name="test_name"
)
result = dti.astype(str)
expected = Index(
    ["2012-03-06 00:00:00+00:00", "2012-03-06 01:00:00+00:00"],
    dtype=object,
    name="test_name",
)
tm.assert_index_equal(result, expected)
