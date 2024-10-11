# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# empty
empty_frame = DataFrame()

result = empty_frame.apply(func)
assert result.empty
