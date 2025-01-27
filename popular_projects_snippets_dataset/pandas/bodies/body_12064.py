# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_c_parser_only.py
# see gh-16798
#
# Read from a "CSV" that has a column larger than 2GB.
parser = c_parser_only

if parser.low_memory:
    pytest.skip("not a low_memory test")

csv = StringIO("strings\n" + "\n".join(["x" * (1 << 20) for _ in range(2100)]))
df = parser.read_csv(csv)
assert not df.empty
