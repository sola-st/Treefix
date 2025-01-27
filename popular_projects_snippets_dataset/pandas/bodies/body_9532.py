# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_timedeltas.py
# GH34290
expected = Timedelta("2 min").total_seconds()

result = pd.array([Timedelta("2 min")]).total_seconds()[0]
assert result == expected
