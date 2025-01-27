# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
gt = DataFrame(np.random.randn(10, 2))
gt.to_excel(path)

with ExcelFile(path) as xl:
    df = pd.read_excel(xl, sheet_name=0, index_col=0)

tm.assert_frame_equal(gt, df)

msg = "Worksheet named '0' not found"
with pytest.raises(ValueError, match=msg):
    pd.read_excel(xl, "0")
