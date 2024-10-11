# Extracted from ./data/repos/pandas/pandas/tests/frame/test_iteration.py
for k, v in float_string_frame.items():
    assert v.name == k
