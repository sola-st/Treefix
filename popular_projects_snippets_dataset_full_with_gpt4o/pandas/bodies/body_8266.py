# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_astype.py
# GH 13149, GH 13209
# verify that we are returning NaT as a string (and not unicode)

idx = DatetimeIndex(["2016-05-16", "NaT", NaT, np.NaN])
result = idx.astype(str)
expected = Index(["2016-05-16", "NaT", "NaT", "NaT"], dtype=object)
tm.assert_index_equal(result, expected)
