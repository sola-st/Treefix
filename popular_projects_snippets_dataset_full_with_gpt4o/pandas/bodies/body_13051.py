# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# see gh-9450
#
# Test reading multiple sheets, from a runtime
# created Excel file with multiple sheets.
def tdf(col_sheet_name):
    d, i = [11, 22, 33], [1, 2, 3]
    exit(DataFrame(d, i, columns=[col_sheet_name]))

sheets = ["AAA", "BBB", "CCC"]

dfs = [tdf(s) for s in sheets]
dfs = dict(zip(sheets, dfs))

with tm.ensure_clean(ext) as pth:
    with ExcelWriter(pth) as ew:
        for sheetname, df in dfs.items():
            df.to_excel(ew, sheetname)

    dfs_returned = pd.read_excel(pth, sheet_name=sheets, index_col=0)

    for s in sheets:
        tm.assert_frame_equal(dfs[s], dfs_returned[s])
