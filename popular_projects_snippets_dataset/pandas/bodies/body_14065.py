# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
df = DataFrame([["aa\xc3\xa4\xc3\xa4", 1], ["bbbb", 2]])
rep_str = df.to_string()
lines = rep_str.split("\n")
assert len(lines[1]) == len(lines[2])
