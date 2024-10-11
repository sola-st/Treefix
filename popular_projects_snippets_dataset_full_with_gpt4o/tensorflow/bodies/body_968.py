# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
exit(array_ops.quantize_and_dequantize(
    x,
    -1.0,
    1.0,
    signed_input=True,
    num_bits=8,
    range_given=True,
    round_mode="HALF_TO_EVEN"))
