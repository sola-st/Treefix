# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
exit(array_ops.quantize_and_dequantize_v3(
    x, -127, 127, num_bits=8, signed_input=True, range_given=False))
