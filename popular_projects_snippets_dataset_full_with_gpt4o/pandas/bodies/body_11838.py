# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_read_errors.py
# see gh-15925
parser = all_parsers
data = """1,2
a,b
a,b,c
a,b,d
a,b
"""
expected = DataFrame({"1": "a", "2": ["b"] * 2})

result = parser.read_csv(StringIO(data), on_bad_lines="warn")
tm.assert_frame_equal(result, expected)

captured = capsys.readouterr()
if parser.engine == "c":
    warn = """Skipping line 3: expected 2 fields, saw 3
Skipping line 4: expected 2 fields, saw 3

"""
else:
    warn = """Skipping line 3: Expected 2 fields in line 3, saw 3
Skipping line 4: Expected 2 fields in line 4, saw 3
"""
assert captured.err == warn
