# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
df = DataFrame(np.random.randn(10, 4))
df.index.name = "foo"

df.to_excel(path, merge_cells=merge_cells)

with ExcelFile(path) as xf:
    result = pd.read_excel(xf, sheet_name=xf.sheet_names[0], index_col=0)

tm.assert_frame_equal(result, df)
assert result.index.name == "foo"
