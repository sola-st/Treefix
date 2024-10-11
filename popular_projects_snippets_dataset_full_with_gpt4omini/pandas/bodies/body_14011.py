# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_series_info.py
index = lexsorted_two_level_string_multiindex
ser = Series(range(len(index)), index=index, name="sth")
buf = StringIO()
ser.info(verbose=verbose, buf=buf)
result = buf.getvalue()

expected = textwrap.dedent(
    """\
        <class 'pandas.core.series.Series'>
        MultiIndex: 10 entries, ('foo', 'one') to ('qux', 'three')
        """
)
if verbose:
    expected += textwrap.dedent(
        """\
            Series name: sth
            Non-Null Count  Dtype
            --------------  -----
            10 non-null     int64
            """
    )
expected += textwrap.dedent(
    f"""\
        dtypes: int64(1)
        memory usage: {ser.memory_usage()}.0+ bytes
        """
)
assert result == expected
