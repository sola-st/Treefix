# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_copy.py
cop = float_frame.copy()
cop["E"] = cop["A"]
assert "E" not in float_frame

# copy objects
copy = float_string_frame.copy()
assert copy._mgr is not float_string_frame._mgr
