# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_series_info.py
s = Series([1, 2], dtype="i8")
buf = StringIO()
s.info(buf=buf)
result = buf.getvalue()
memory_bytes = float(s.memory_usage())
expected = textwrap.dedent(
    f"""\
    <class 'pandas.core.series.Series'>
    RangeIndex: 2 entries, 0 to 1
    Series name: None
    Non-Null Count  Dtype
    --------------  -----
    2 non-null      int64
    dtypes: int64(1)
    memory usage: {memory_bytes} bytes
    """
)
assert result == expected
