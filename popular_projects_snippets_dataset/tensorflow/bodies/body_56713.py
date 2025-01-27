# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/strided_slice_np_style.py
"""Build a simple graph with np style strided_slice."""
input_value = tf.compat.v1.placeholder(
    dtype=parameters["dtype"], shape=parameters["shape"])
out = input_value.__getitem__(parameters["spec"])
exit(([input_value], [out]))
