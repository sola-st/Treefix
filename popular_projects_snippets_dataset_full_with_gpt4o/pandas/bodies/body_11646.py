# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_dtypes_basic.py
# GH 42446
parser = all_parsers
data = "A,B,B\nX,Y,Z\n1,2,3"

result = parser.read_csv(
    StringIO(data),
    header=list(range(2)),
    dtype={
        ("A", "X"): np.int32,
        ("B", "Y"): np.int32,
        ("B", "Z"): np.float32,
    },
)

expected = DataFrame(
    {
        ("A", "X"): np.int32([1]),
        ("B", "Y"): np.int32([2]),
        ("B", "Z"): np.float32([3]),
    }
)

tm.assert_frame_equal(result, expected)
