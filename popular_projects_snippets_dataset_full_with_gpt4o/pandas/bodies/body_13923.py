# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_info.py
# GH #45494
df = DataFrame()
buf = StringIO()
df.info(buf=buf)
result = buf.getvalue()
expected = textwrap.dedent(
    """\
        <class 'pandas.core.frame.DataFrame'>
        RangeIndex: 0 entries
        Empty DataFrame\n"""
)
assert result == expected
