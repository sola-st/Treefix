# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_compression.py
parser = all_parsers

with open(csv1, "rb") as f:
    data = f.read()
expected = parser.read_csv(csv1)

exit((parser, data, expected))
