# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# GH 12617

# should preserve name
s = Series(["a,b", "c,d"], name="xxx", dtype=any_string_dtype)
res = s.str.split(",")
exp = Series([["a", "b"], ["c", "d"]], name="xxx")
tm.assert_series_equal(res, exp)

res = s.str.split(",", expand=True)
exp = DataFrame([["a", "b"], ["c", "d"]], dtype=any_string_dtype)
tm.assert_frame_equal(res, exp)
