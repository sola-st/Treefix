# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
# GH 12163
expected = Series(dtype=object), MyTz()
result = tm.round_trip_pickle(expected)

tm.assert_series_equal(result[0], expected[0])
assert isinstance(result[1], MyTz)
