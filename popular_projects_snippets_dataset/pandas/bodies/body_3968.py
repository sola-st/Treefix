# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
s = float_frame["A"]
assert s.name == "A"

s = float_frame.pop("A")
assert s.name == "A"

s = float_frame.loc[:, "B"]
assert s.name == "B"

s2 = s.loc[:]
assert s2.name == "B"
