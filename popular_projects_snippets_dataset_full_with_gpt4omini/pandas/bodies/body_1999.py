# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# see gh-13352
data = ["1", 2, 3]
invalid_downcast = "unsigned-integer"
msg = "invalid downcasting method provided"

with pytest.raises(ValueError, match=msg):
    to_numeric(data, downcast=invalid_downcast)
