# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_categorical.py
# see gh-10153
pth = os.path.join(csv_dir_path, "utf16_ex.txt")
parser = all_parsers
encoding = "utf-16"
sep = "\t"

expected = parser.read_csv(pth, sep=sep, encoding=encoding)
expected = expected.apply(Categorical)

actual = parser.read_csv(pth, sep=sep, encoding=encoding, dtype="category")
tm.assert_frame_equal(actual, expected)
