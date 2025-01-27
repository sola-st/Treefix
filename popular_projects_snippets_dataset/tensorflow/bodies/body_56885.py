# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/reverse_sequence.py
"""Build the graph for reverse_sequence tests."""
input_value = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])
outs = tf.reverse_sequence(
    input=input_value,
    seq_lengths=parameters["seq_lengths"],
    batch_axis=parameters["batch_axis"],
    seq_axis=parameters["seq_axis"])
exit(([input_value], [outs]))
