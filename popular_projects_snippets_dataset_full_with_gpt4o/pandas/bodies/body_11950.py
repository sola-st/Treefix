# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
data = """A,B,C
True,False,True
NA,True,False
False,NA,True"""
parser = all_parsers
result = parser.read_csv(StringIO(data))
expected = DataFrame(
    {
        "A": np.array([True, np.nan, False], dtype=object),
        "B": np.array([False, True, np.nan], dtype=object),
        "C": [True, False, True],
    }
)
tm.assert_frame_equal(result, expected)
