# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# usecols as int
msg = "Passing an integer for `usecols`"
with pytest.raises(ValueError, match=msg):
    pd.read_excel(
        "test1" + read_ext, sheet_name="Sheet1", index_col=0, usecols=3
    )

# usecols as int
with pytest.raises(ValueError, match=msg):
    pd.read_excel(
        "test1" + read_ext,
        sheet_name="Sheet2",
        skiprows=[1],
        index_col=0,
        usecols=3,
    )
