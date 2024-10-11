# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
exit(array_ops.quantize_and_dequantize(
    x, -127, 127, signed_input=True, num_bits=8))
