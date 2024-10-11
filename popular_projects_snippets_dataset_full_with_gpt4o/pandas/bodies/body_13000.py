# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH 16645
msg = "'nrows' must be an integer >=0"
with pytest.raises(ValueError, match=msg):
    pd.read_excel("test1" + read_ext, nrows="5")
