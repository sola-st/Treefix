# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py

# GH31467
str_path = os.path.join("test1" + read_ext)
with open(str_path, "rb") as f:
    x = pd.read_excel(f, sheet_name="Sheet1", index_col=0)
    del x
    # should not throw an exception because the passed file was closed
    f.read()
