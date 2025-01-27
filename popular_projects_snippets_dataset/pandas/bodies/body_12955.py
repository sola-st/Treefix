# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
msg = (
    "Usecols do not match columns, "
    "columns expected but not found: " + r"\['E'\]"
)

with pytest.raises(ValueError, match=msg):
    pd.read_excel("test1" + read_ext, usecols=["E"])
