# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# vector-like others are tested in test_td64arr_add_sub_numeric_arr_invalid
tdser = Series(["59 Days", "59 Days", "NaT"], dtype="m8[ns]")
tdarr = tm.box_expected(tdser, box_with_array)

assert_invalid_addsub_type(tdarr, other)
