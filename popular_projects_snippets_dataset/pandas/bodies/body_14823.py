# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
ser = Series(range(1))
msg = "An iterable subplots for a Series"
with pytest.raises(NotImplementedError, match=msg):
    ser.plot(subplots=[("a",)])
