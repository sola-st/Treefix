# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_info.py
# GH#37245
df = DataFrame({1: [1, 2], 2: [2, 3]}, index=["A", "B"])
buf = StringIO()
df.info(show_counts=True, buf=buf)
result = buf.getvalue()
expected = textwrap.dedent(
    """\
        <class 'pandas.core.frame.DataFrame'>
        Index: 2 entries, A to B
        Data columns (total 2 columns):
         #   Column  Non-Null Count  Dtype
        ---  ------  --------------  -----
         0   1       2 non-null      int64
         1   2       2 non-null      int64
        dtypes: int64(2)
        memory usage: 48.0+ bytes
        """
)
assert result == expected
