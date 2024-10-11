# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# GH#45793
with tm.ensure_clean(ext) as path:
    DataFrame().to_excel(path, engine=engine)
    result = pd.read_excel(path)
    expected = DataFrame()
    tm.assert_frame_equal(result, expected)
