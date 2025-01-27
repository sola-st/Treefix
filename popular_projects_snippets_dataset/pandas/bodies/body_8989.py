# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
obj = request.getfixturevalue(fix)
unpickled = tm.round_trip_pickle(obj)
tm.assert_sp_array_equal(unpickled, obj)
