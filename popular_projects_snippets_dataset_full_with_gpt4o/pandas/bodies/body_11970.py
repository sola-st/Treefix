# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
# GH 42446
parser = all_parsers
data = "A,B,B\nX,Y,Z\n1,2,inf"

result = parser.read_csv(
    StringIO(data), header=list(range(2)), na_values={("B", "Z"): "inf"}
)

expected = DataFrame(
    {
        ("A", "X"): [1],
        ("B", "Y"): [2],
        ("B", "Z"): [np.nan],
    }
)

tm.assert_frame_equal(result, expected)
