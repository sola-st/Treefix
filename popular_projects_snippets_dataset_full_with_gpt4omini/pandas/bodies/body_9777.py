# Extracted from ./data/repos/pandas/pandas/tests/window/test_win_type.py
# GH 48838
freq_roll = Series(range(2), index=date_range("2020", periods=2)).rolling("2s")
assert freq_roll.win_type is None
