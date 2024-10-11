# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
url = (
    "https://raw.githubusercontent.com/pandas-dev/pandas/main/"
    "pandas/tests/io/data/excel/test1" + read_ext
)
url_table = pd.read_excel(url)
local_table = pd.read_excel("test1" + read_ext)
tm.assert_frame_equal(url_table, local_table)
