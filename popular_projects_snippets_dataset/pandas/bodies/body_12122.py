# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_encoding.py
"""
    Chunk splits a multibyte character with memory_map=True

    GH 43540
    """
parser = all_parsers
# DEFAULT_CHUNKSIZE = 262144, defined in parsers.pyx
df = DataFrame(data=["a" * 127] * 2048)

# Put two-bytes utf-8 encoded character "ą" at the end of chunk
# utf-8 encoding of "ą" is b'\xc4\x85'
df.iloc[2047] = "a" * 127 + "ą"
with tm.ensure_clean("bug-gh43540.csv") as fname:
    df.to_csv(fname, index=False, header=False, encoding="utf-8")
    dfr = parser.read_csv(fname, header=None, memory_map=True, engine="c")
tm.assert_frame_equal(dfr, df)
