# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
buf = StringIO()

unicode_values = ["\u03c3"] * 10
unicode_values = np.array(unicode_values, dtype=object)
df = DataFrame({"unicode": unicode_values})
df.to_string(col_space=10, buf=buf)

# it works!
repr(df)

idx = Index(["abc", "\u03c3a", "aegdvg"])
ser = Series(np.random.randn(len(idx)), idx)
rs = repr(ser).split("\n")
line_len = len(rs[0])
for line in rs[1:]:
    try:
        line = line.decode(get_option("display.encoding"))
    except AttributeError:
        pass
    if not line.startswith("dtype:"):
        assert len(line) == line_len

        # it works even if sys.stdin in None
_stdin = sys.stdin
try:
    sys.stdin = None
    repr(df)
finally:
    sys.stdin = _stdin
