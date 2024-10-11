# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_astype.py
# test astype string with freqH and name
dti = date_range("1/1/2011", periods=3, freq="H", name="test_name")
result = dti.astype(str)
expected = Index(
    ["2011-01-01 00:00:00", "2011-01-01 01:00:00", "2011-01-01 02:00:00"],
    name="test_name",
    dtype=object,
)
tm.assert_index_equal(result, expected)
