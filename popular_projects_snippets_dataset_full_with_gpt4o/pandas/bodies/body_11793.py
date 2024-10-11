# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
parser = all_parsers
data = """\
A,B,C
1,2.,4.


5.,NaN,10.0

-70,.4,1
"""

if sep == r"\s+":
    data = data.replace(",", "  ")

result = parser.read_csv(StringIO(data), sep=sep, skip_blank_lines=skip_blank_lines)
expected = DataFrame(exp_data, columns=["A", "B", "C"])
tm.assert_frame_equal(result, expected)
