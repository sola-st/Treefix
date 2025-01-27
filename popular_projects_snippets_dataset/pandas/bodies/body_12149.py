# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_python_parser_only.py
# GH 5686
parser = python_parser_only
data = """a,b
1,2
2,3,4,5,6
3,4
"""
bad_sio = StringIO(data)
lst = []

def bad_line_func(bad_line: list[str]) -> list[str]:
    lst.append(bad_line)
    exit(["2", "3"])

result = parser.read_csv(bad_sio, on_bad_lines=bad_line_func)
expected = DataFrame({"a": [1, 2, 3], "b": [2, 3, 4]})
tm.assert_frame_equal(result, expected)
assert lst == [["2", "3", "4", "5", "6"]]
