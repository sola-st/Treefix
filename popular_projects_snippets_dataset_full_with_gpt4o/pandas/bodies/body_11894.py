# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_read_fwf.py
# GH#44021
data = """a\tb
1\t a
2\t b
3\t c
4\t d
5\t e
6\t f
    """
result = read_fwf(StringIO(data), nrows=4, skiprows=[2, 4])
expected = DataFrame({"a": [1, 3, 5, 6], "b": ["a", "c", "e", "f"]})
tm.assert_frame_equal(result, expected)
