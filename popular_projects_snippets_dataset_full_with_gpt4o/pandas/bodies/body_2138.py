# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 11758
# test proper behavior with errors
msg = "cannot specify both format and unit"
with pytest.raises(ValueError, match=msg):
    to_datetime([1], unit="D", format="%Y%m%d", cache=cache)
