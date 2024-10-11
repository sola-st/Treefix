# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
df = DataFrame(123, index=range(10, 15), columns=range(30))
s = df.to_string(line_width=80)
assert max(len(line) for line in s.split("\n")) == 80
