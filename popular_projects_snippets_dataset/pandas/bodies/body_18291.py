# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_object.py
# GH#17067, GH#19723 __iadd__ and __isub__ should preserve index name
ser = Series([1, 2, 3])
ser.index.name = "foo"

ser.index += 1
assert ser.index.name == "foo"

ser.index -= 1
assert ser.index.name == "foo"
