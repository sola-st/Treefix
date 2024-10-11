# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
# GH 23803
with pytest.raises(ValueError, match="na_action must be .*Got 'abc'"):
    float_frame.applymap(lambda x: len(str(x)), na_action="abc")
