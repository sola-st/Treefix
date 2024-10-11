# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
msg = "list indices must be integers.*, not str"

with pytest.raises(TypeError, match=msg):
    pd.read_excel(
        "test1" + read_ext,
        sheet_name="Sheet1",
        index_col=["A"],
        usecols=["A", "C"],
    )
