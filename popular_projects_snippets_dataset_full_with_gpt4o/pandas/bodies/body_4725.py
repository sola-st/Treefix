# Extracted from ./data/repos/pandas/pandas/tests/strings/test_extract.py
# single group renames series/index properly
s_or_idx = index_or_series(["A1", "A2"], dtype=any_string_dtype)
result = s_or_idx.str.extract(r"(?P<uno>A)\d", expand=True)
expected = DataFrame({"uno": ["A", "A"]}, dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
