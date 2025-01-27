# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_float.py
# GH#38753
parser, precision = all_parsers_all_precisions

data = f"data\n10E{neg_exp}"
result = parser.read_csv(StringIO(data), float_precision=precision)
expected = DataFrame({"data": [0.0]})
tm.assert_frame_equal(result, expected)
