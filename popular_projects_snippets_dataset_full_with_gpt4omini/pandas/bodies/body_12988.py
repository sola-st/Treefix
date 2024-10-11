# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py

# GH12655
from py.path import local as LocalPath

str_path = os.path.join("test1" + read_ext)
expected = pd.read_excel(str_path, sheet_name="Sheet1", index_col=0)

path_obj = LocalPath().join("test1" + read_ext)
actual = pd.read_excel(path_obj, sheet_name="Sheet1", index_col=0)

tm.assert_frame_equal(expected, actual)
