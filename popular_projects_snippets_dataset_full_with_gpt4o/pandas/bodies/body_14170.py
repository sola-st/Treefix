# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
delta_1d = pd.to_timedelta(1, unit="D")
delta_0d = pd.to_timedelta(0, unit="D")
delta_1s = pd.to_timedelta(1, unit="s")
delta_500ms = pd.to_timedelta(500, unit="ms")

drepr = lambda x: x._repr_base()
assert drepr(delta_1d) == "1 days"
assert drepr(-delta_1d) == "-1 days"
assert drepr(delta_0d) == "0 days"
assert drepr(delta_1s) == "0 days 00:00:01"
assert drepr(delta_500ms) == "0 days 00:00:00.500000"
assert drepr(delta_1d + delta_1s) == "1 days 00:00:01"
assert drepr(-delta_1d + delta_1s) == "-1 days +00:00:01"
assert drepr(delta_1d + delta_500ms) == "1 days 00:00:00.500000"
assert drepr(-delta_1d + delta_500ms) == "-1 days +00:00:00.500000"
