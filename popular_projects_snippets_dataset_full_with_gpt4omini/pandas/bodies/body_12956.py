# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
msg = (
    "'usecols' must either be list-like of "
    "all strings, all unicode, all integers or a callable."
)

with pytest.raises(ValueError, match=msg):
    pd.read_excel("test1" + read_ext, usecols=["E1", 0])
