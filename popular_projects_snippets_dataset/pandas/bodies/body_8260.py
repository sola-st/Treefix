# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_insert.py
# GH#33703
tz = tz_aware_fixture
dti = date_range("2019-11-04", periods=3, freq="-1D", name=9, tz=tz)

value = "foo"
result = dti.insert(0, value)

expected = Index(["foo"] + list(dti), dtype=object, name=9)
tm.assert_index_equal(result, expected)
