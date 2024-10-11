# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
expected_format = "%Y-%m-%d %H:%M:%S.%f"
test_array = np.array(test_list, dtype=object)
assert tools._guess_datetime_format_for_array(test_array) == expected_format
