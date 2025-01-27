# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH 26566
msg = "Engine should not be specified when passing an ExcelFile"

with pd.ExcelFile("test1" + read_ext) as xl:
    with pytest.raises(ValueError, match=msg):
        pd.read_excel(xl, engine="foo")
