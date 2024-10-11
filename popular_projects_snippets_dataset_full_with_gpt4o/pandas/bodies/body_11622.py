# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_categorical.py
# see gh-10153
pth = os.path.join(csv_dir_path, "unicode_series.csv")
parser = all_parsers
encoding = "latin-1"

expected = parser.read_csv(pth, header=None, encoding=encoding)
expected[1] = Categorical(expected[1])

actual = parser.read_csv(pth, header=None, encoding=encoding, dtype={1: "category"})
tm.assert_frame_equal(actual, expected)
