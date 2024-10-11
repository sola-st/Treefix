# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# GH 13228
ser = Series(1 / 3)
result = ser.map(lambda val: str(val)).to_dict()
expected = {0: "0.3333333333333333"}
assert result == expected
