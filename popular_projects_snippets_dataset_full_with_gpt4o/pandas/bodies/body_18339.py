# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
tdser = Series(["59 Days", "59 Days", "NaT"], dtype="m8[ns]")
tdarr = tm.box_expected(tdser, box_with_array)

vector = vec.astype(any_real_numpy_dtype)
assert_invalid_addsub_type(tdarr, vector)
