# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_textreader.py
# GH14867
with read_csv(
    StringIO(), chunksize=20, header=None, names=["a", "b", "c"]
) as df:
    assert isinstance(df, TextFileReader)
