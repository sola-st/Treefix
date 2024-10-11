# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_compression.py
parser = all_parsers
path = os.path.join(csv_dir_path, "tar_csv.tar.gz")
df = parser.read_csv(path)
assert list(df.columns) == ["a"]
