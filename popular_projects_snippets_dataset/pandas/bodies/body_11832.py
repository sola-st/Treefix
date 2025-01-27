# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_read_errors.py
# see gh-15925
parser = all_parsers
data = "a\n1\n1,2,3\n4\n5,6,7"
expected = DataFrame({"a": [1, 4]})

result = parser.read_csv(StringIO(data), on_bad_lines="warn")
tm.assert_frame_equal(result, expected)

captured = capsys.readouterr()
assert "Skipping line 3" in captured.err
assert "Skipping line 5" in captured.err
