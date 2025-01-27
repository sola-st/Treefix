# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
# https://github.com/pandas-dev/pandas/issues/46588
s = Series([1, 2, 3])
msg = f"na_action must either be 'ignore' or None, {input_na_action} was passed"
with pytest.raises(ValueError, match=msg):
    s.map({1: 2}, na_action=input_na_action)
