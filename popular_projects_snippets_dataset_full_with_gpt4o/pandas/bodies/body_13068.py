# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
frame = frame.copy()
frame.iloc[:5, frame.columns.get_loc("A")] = np.nan

frame.to_excel(path, "test1")
frame.to_excel(path, "test1", columns=["A", "B"])
frame.to_excel(path, "test1", header=False)
frame.to_excel(path, "test1", index=False)

# column aliases
col_aliases = Index(["AA", "X", "Y", "Z"])
frame.to_excel(path, "test1", header=col_aliases)
with ExcelFile(path) as reader:
    rs = pd.read_excel(reader, sheet_name="test1", index_col=0)
xp = frame.copy()
xp.columns = col_aliases
tm.assert_frame_equal(xp, rs)
