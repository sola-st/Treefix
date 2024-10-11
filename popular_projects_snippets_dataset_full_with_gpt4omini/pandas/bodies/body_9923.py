# Extracted from ./data/repos/pandas/pandas/tests/window/test_api.py
# GH 39554
roll_obj = Series(range(1)).rolling(
    1, center=center, closed=closed, min_periods=min_periods, step=step
)
expected = {attr: getattr(roll_obj, attr) for attr in roll_obj._attributes}
getattr(roll_obj, arithmetic_win_operators)()
result = {attr: getattr(roll_obj, attr) for attr in roll_obj._attributes}
assert result == expected
