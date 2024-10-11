# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py

# FILE
localtable = os.path.join(datapath("io", "data", "excel"), "test1" + read_ext)
local_table = pd.read_excel(localtable)

try:
    url_table = pd.read_excel("file://localhost/" + localtable)
except URLError:
    # fails on some systems
    platform_info = " ".join(platform.uname()).strip()
    pytest.skip(f"failing on {platform_info}")

tm.assert_frame_equal(url_table, local_table)
