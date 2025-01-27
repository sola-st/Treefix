# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
# https://github.com/pandas-dev/pandas/issues/32815
s = Series([1, 2, 3])
msg = "na_action must either be 'ignore' or None"
with pytest.raises(ValueError, match=msg):
    s.map(lambda x: x, na_action="____")
