# Extracted from ./data/repos/pandas/pandas/tests/frame/test_block_internals.py
frame = float_frame.copy()  # noqa

# triggers in-place consolidation
for letter in range(ord("A"), ord("Z")):
    float_frame[chr(letter)] = chr(letter)
