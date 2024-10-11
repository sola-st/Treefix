# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_converters.py
# see gh-2184
parser = all_parsers
data = """000102,1.2,A\n001245,2,B"""

converters = {0: lambda x: x.strip()}
result = parser.read_csv(StringIO(data), header=None, converters=converters)

# Column 0 should not be casted to numeric and should remain as object.
expected = DataFrame([["000102", 1.2, "A"], ["001245", 2, "B"]])
tm.assert_frame_equal(result, expected)
