# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH13176
msg = "is not convertible to datetime"
with pytest.raises(TypeError, match=msg):
    to_datetime(arg)
