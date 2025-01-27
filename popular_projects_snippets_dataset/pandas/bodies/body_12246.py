# Extracted from ./data/repos/pandas/pandas/tests/io/test_fsspec.py
pytest.importorskip("openpyxl")
ext = "xlsx"
path = f"memory://test/test.{ext}"
df1.to_excel(path, index=True)

df2 = read_excel(path, parse_dates=["dt"], index_col=0)

tm.assert_frame_equal(df1, df2)
