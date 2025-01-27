# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_astype.py
# GH 20997, 20964, 24559
val = [Timestamp("2018-01-01", tz=tz).as_unit("ns").value]
result = Index(val, name="idx").astype(dtype)
expected = DatetimeIndex(["2018-01-01"], tz=tz, name="idx")
tm.assert_index_equal(result, expected)
