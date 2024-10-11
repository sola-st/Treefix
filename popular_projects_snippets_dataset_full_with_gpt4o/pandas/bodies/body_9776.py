# Extracted from ./data/repos/pandas/pandas/tests/window/test_win_type.py
# GH 15969
s = Series(range(1))
with pytest.raises(ValueError, match="Invalid win_type freq"):
    s.rolling(arg, win_type="freq")
