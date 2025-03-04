# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_dict_compat.py
data_datetime64 = {np.datetime64("1990-03-15"): 1, np.datetime64("2015-03-15"): 2}
data_unchanged = {1: 2, 3: 4, 5: 6}
expected = {Timestamp("1990-3-15"): 1, Timestamp("2015-03-15"): 2}
assert dict_compat(data_datetime64) == expected
assert dict_compat(expected) == expected
assert dict_compat(data_unchanged) == data_unchanged
