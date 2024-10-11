# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/binary_op.py
"""Return a function that does a test on a binary operator."""
exit(lambda options: make_binary_op_tests(options, binary_operator))
