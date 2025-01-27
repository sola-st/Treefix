# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_decimal.py
parser = all_parsers
expected = DataFrame({"A": [1, 10], "B": [2334.01, 13], "C": [5, 10.0]})

result = parser.read_csv(
    StringIO(data), sep="|", thousands=thousands, decimal=decimal
)
tm.assert_frame_equal(result, expected)
