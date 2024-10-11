# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# see gh-16893
filename = os.path.join(csv_dir_path, "sub_char.csv")
expected = DataFrame([[1, 2, 3]], columns=["a", "\x1ab", "c"])

parser = all_parsers
result = parser.read_csv(filename)
tm.assert_frame_equal(result, expected)
