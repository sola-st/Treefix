# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
result = to_datetime([arg], cache=cache)
exp = Timestamp(exp_str)
assert result[0] == exp
