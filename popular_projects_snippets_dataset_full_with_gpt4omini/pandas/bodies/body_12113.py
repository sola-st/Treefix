# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_encoding.py
path = os.path.join(csv_dir_path, "unicode_series.csv")
parser = all_parsers

result = parser.read_csv(path, header=None, encoding="latin-1")
result = result.set_index(0)
got = result[1][1632]

expected = "\xc1 k\xf6ldum klaka (Cold Fever) (1994)"
assert got == expected
