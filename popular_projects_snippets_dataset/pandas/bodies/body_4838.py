# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
s = Series(["nosplit", "alsonosplit"], dtype=any_string_dtype)
result = s.str.rsplit("_", expand=True)
exp = DataFrame({0: Series(["nosplit", "alsonosplit"])}, dtype=any_string_dtype)
tm.assert_frame_equal(result, exp)
