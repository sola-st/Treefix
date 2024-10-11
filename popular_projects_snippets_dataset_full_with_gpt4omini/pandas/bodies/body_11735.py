# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_ints.py
data = """Numbers
17007000002000191
17007000002000191
17007000002000191
17007000002000191
17007000002000192
17007000002000192
17007000002000192
17007000002000192
17007000002000192
17007000002000194"""
parser = all_parsers
result = parser.read_csv(StringIO(data))
expected = DataFrame(
    {
        "Numbers": [
            17007000002000191,
            17007000002000191,
            17007000002000191,
            17007000002000191,
            17007000002000192,
            17007000002000192,
            17007000002000192,
            17007000002000192,
            17007000002000192,
            17007000002000194,
        ]
    }
)
tm.assert_frame_equal(result, expected)
