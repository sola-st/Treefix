# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# Issue #24861
tm.reset_display_options()
df = DataFrame(
    {
        "A": [-np.inf, np.inf, -1, -2.1234, 3, 4],
        "B": [-np.inf, np.inf, "foo", "foooo", "fooooo", "bar"],
    }
)
result = df.to_string()

expected = (
    "        A       B\n"
    "0    -inf    -inf\n"
    "1     inf     inf\n"
    "2 -1.0000     foo\n"
    "3 -2.1234   foooo\n"
    "4  3.0000  fooooo\n"
    "5  4.0000     bar"
)
assert result == expected

df = DataFrame(
    {
        "A": [-np.inf, np.inf, -1.0, -2.0, 3.0, 4.0],
        "B": [-np.inf, np.inf, "foo", "foooo", "fooooo", "bar"],
    }
)
result = df.to_string()

expected = (
    "     A       B\n"
    "0 -inf    -inf\n"
    "1  inf     inf\n"
    "2 -1.0     foo\n"
    "3 -2.0   foooo\n"
    "4  3.0  fooooo\n"
    "5  4.0     bar"
)
assert result == expected
