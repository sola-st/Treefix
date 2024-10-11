# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# GH48646
parser = all_parsers
prefix = "### DATA\n"
content = "nkey,value\ntables,rectangular\n"
with tm.ensure_clean() as path:
    Path(path).write_text(prefix + content)
    with open(path, encoding="utf-8") as file:
        file.readline()
        actual = parser.read_csv(file)
    expected = parser.read_csv(StringIO(content))
tm.assert_frame_equal(actual, expected)
