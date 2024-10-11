# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
data = """A,B,C
foo,bar,NA
bar,foo,foo
foo,bar,NA
bar,foo,foo"""
parser = all_parsers
df = parser.read_csv(StringIO(data), na_values={"A": ["foo"], "B": ["bar"]})
expected = DataFrame(
    {
        "A": [np.nan, "bar", np.nan, "bar"],
        "B": [np.nan, "foo", np.nan, "foo"],
        "C": [np.nan, "foo", np.nan, "foo"],
    }
)
tm.assert_frame_equal(df, expected)
