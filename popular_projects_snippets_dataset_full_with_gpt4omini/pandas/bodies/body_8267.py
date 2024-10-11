# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_astype.py
# test astype string - #10442
dti = date_range("2012-01-01", periods=4, name="test_name")
result = dti.astype(str)
expected = Index(
    ["2012-01-01", "2012-01-02", "2012-01-03", "2012-01-04"],
    name="test_name",
    dtype=object,
)
tm.assert_index_equal(result, expected)
