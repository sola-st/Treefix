# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_arithmetic.py
msg = (
    r"numpy boolean subtract, the `-` operator, is (?:deprecated|not supported), "
    r"use the bitwise_xor, the `\^` operator, or the logical_xor function instead\."
)
with pytest.raises(TypeError, match=msg):
    left_array - right_array
