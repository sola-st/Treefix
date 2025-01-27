# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
# 0x00bc: ¼ VULGAR FRACTION ONE QUARTER
# 0x2605: ★ not number
# 0x1378: ፸ ETHIOPIC NUMBER SEVENTY
# 0xFF13: ３ Em 3
ser = Series(["A", "3", "¼", "★", "፸", "３", "four"], dtype=any_string_dtype)
expected_dtype = "bool" if any_string_dtype == "object" else "boolean"
expected = Series(expected, dtype=expected_dtype)
result = getattr(ser.str, method)()
tm.assert_series_equal(result, expected)

# compare with standard library
expected = [getattr(item, method)() for item in ser]
assert list(result) == expected
