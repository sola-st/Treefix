# Extracted from ./data/repos/pandas/pandas/tests/window/test_win_type.py
# This error is raised by scipy
msg = r"boxcar\(\) got an unexpected"
with pytest.raises(TypeError, match=msg):
    Series(range(3)).rolling(1, win_type="boxcar").mean(foo="bar")
