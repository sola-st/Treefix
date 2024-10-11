# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
frame = frame.copy()
frame.iloc[:5, frame.columns.get_loc("A")] = np.nan

frame.to_excel(path, "test1")
frame.to_excel(path, "test1", columns=["A", "B"])
frame.to_excel(path, "test1", header=False)
frame.to_excel(path, "test1", index=False)

# test index_label
df = DataFrame(np.random.randn(10, 2)) >= 0
df.to_excel(path, "test1", index_label=["test"], merge_cells=merge_cells)
with ExcelFile(path) as reader:
    recons = pd.read_excel(reader, sheet_name="test1", index_col=0).astype(
        np.int64
    )
df.index.names = ["test"]
assert df.index.names == recons.index.names

df = DataFrame(np.random.randn(10, 2)) >= 0
df.to_excel(
    path,
    "test1",
    index_label=["test", "dummy", "dummy2"],
    merge_cells=merge_cells,
)
with ExcelFile(path) as reader:
    recons = pd.read_excel(reader, sheet_name="test1", index_col=0).astype(
        np.int64
    )
df.index.names = ["test"]
assert df.index.names == recons.index.names

df = DataFrame(np.random.randn(10, 2)) >= 0
df.to_excel(path, "test1", index_label="test", merge_cells=merge_cells)
with ExcelFile(path) as reader:
    recons = pd.read_excel(reader, sheet_name="test1", index_col=0).astype(
        np.int64
    )
df.index.names = ["test"]
tm.assert_frame_equal(df, recons.astype(bool))

frame.to_excel(
    path,
    "test1",
    columns=["A", "B", "C", "D"],
    index=False,
    merge_cells=merge_cells,
)
# take 'A' and 'B' as indexes (same row as cols 'C', 'D')
df = frame.copy()
df = df.set_index(["A", "B"])

with ExcelFile(path) as reader:
    recons = pd.read_excel(reader, sheet_name="test1", index_col=[0, 1])
tm.assert_frame_equal(df, recons)
