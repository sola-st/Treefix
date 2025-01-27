# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
bad_engine = "foo"
with pytest.raises(ValueError, match="Unknown engine: foo"):
    pd.read_excel("", engine=bad_engine)
