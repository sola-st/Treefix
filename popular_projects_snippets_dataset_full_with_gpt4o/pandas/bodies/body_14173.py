# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
delta_1d = pd.to_timedelta(1, unit="D")
delta_0d = pd.to_timedelta(0, unit="D")
delta_1ns = pd.to_timedelta(1, unit="ns")

drepr = lambda x: x._repr_base(format="all")
assert drepr(delta_1d) == "1 days 00:00:00.000000000"
assert drepr(-delta_1d) == "-1 days +00:00:00.000000000"
assert drepr(delta_0d) == "0 days 00:00:00.000000000"
assert drepr(delta_1ns) == "0 days 00:00:00.000000001"
assert drepr(-delta_1d + delta_1ns) == "-1 days +00:00:00.000000001"
