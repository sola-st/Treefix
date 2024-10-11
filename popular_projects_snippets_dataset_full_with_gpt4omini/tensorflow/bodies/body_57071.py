# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/gather_with_constant.py
"""Build a graph where the inputs to Gather are constants."""
reference = tf.compat.v1.placeholder(
    dtype=tf.int32, shape=parameters["reference_shape"])
gather_input = tf.constant(
    create_tensor_data(tf.int32, parameters["input_shape"]))
gather_indices = tf.constant([0, 1], tf.int32)
out = tf.equal(reference, tf.gather(gather_input, gather_indices))
exit(([reference], [out]))
