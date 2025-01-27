# Extracted from ./data/repos/pandas/pandas/tests/util/test_util.py
rows_list = ["aaa", "bbb", "ccc"]
ret = tm.convert_rows_list_to_csv_str(rows_list)

if compat.is_platform_windows():
    expected = "aaa\r\nbbb\r\nccc\r\n"
else:
    expected = "aaa\nbbb\nccc\n"

assert ret == expected
