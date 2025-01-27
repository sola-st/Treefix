# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
parser = all_parsers
data = """A|B|C
1|2,334|5
10|13|10.
"""
expected = DataFrame({"A": [1, 10], "B": [2334, 13], "C": [5, 10.0]})

result = parser.read_csv(StringIO(data), sep="|", thousands=",")
tm.assert_frame_equal(result, expected)
