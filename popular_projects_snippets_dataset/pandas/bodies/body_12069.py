# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_c_parser_only.py
parser = c_parser_only
expected = DataFrame({"A": [1, 10], "B": [2334.01, 13], "C": [5, 10.0]})

result = parser.read_csv(
    StringIO(data),
    sep="|",
    thousands=thousands,
    decimal=decimal,
    float_precision=float_precision,
)
tm.assert_frame_equal(result, expected)
