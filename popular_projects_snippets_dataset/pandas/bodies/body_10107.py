# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py
frame_result = getattr(frame.ewm(com=10), name)()
assert isinstance(frame_result, DataFrame)
