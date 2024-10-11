# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_delitem.py
del float_frame["A"]
assert "A" not in float_frame
