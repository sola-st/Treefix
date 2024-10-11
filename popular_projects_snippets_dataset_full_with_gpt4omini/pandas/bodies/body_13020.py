# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH 15914
expected = pd.read_excel("test1" + read_ext, engine=engine)

with open("test1" + read_ext, "rb") as f:
    data = f.read()

actual = pd.read_excel(data, engine=engine)
tm.assert_frame_equal(expected, actual)
