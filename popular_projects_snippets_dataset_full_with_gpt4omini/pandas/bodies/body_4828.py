# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# #1859
s = Series(["Wes McKinney", "Travis  Oliphant"], dtype=any_string_dtype)
result = getattr(s.str, method)()
expected = ["Travis", "Oliphant"]
assert result[1] == expected
