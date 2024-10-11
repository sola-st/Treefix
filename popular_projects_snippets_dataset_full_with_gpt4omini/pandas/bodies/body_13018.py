# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
with open("test1" + read_ext, "rb") as f:
    with pd.ExcelFile(f) as xlsx:
        # parses okay
        pd.read_excel(xlsx, sheet_name="Sheet1", index_col=0, engine=engine)

assert f.closed
