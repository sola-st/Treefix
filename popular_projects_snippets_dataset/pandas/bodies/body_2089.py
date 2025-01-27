# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
actual = to_datetime("20080115")
assert actual == datetime(2008, 1, 15)
