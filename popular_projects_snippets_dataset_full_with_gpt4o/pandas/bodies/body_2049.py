# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
# GH: 36738
expected = pd.Timedelta(expected)
result = func(input)
assert result == expected
