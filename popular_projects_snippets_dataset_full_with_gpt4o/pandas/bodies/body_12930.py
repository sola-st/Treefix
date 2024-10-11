# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_openpyxl.py
# GH 39576
df = DataFrame()

with tm.ensure_clean(ext) as f:
    df.to_excel(f, engine="openpyxl")

    with ExcelWriter(
        f, mode="a", engine="openpyxl", if_sheet_exists="new"
    ) as writer:
        df.to_excel(writer)

    # make sure that zip files are not concatenated by making sure that
    # "docProps/app.xml" only occurs twice in the file
    data = Path(f).read_bytes()
    first = data.find(b"docProps/app.xml")
    second = data.find(b"docProps/app.xml", first + 1)
    third = data.find(b"docProps/app.xml", second + 1)
    assert second != -1 and third == -1
