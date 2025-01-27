# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH 38424
with open("test1" + read_ext, "rb") as f:
    result = pd.read_excel(f)
expected = pd.read_excel("test1" + read_ext, engine=engine)
tm.assert_frame_equal(result, expected)
