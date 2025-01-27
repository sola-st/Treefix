# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# https://github.com/pandas-dev/pandas/issues/23558
# compare to standard lib
s = Series(["A_B_C", "B_C_D", "E_F_G", "EFGHEF"], dtype=any_string_dtype)
result = getattr(s.str, method)("_", expand=False).tolist()
assert result == [getattr(v, method)("_") for v in s]
