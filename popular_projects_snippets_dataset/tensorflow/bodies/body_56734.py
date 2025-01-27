# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/segment_sum.py
"""Build the segment_sum op testing graph."""
data = tf.compat.v1.placeholder(
    dtype=parameters["data_dtype"],
    name="data",
    shape=parameters["data_shape"])
segment_ids = tf.constant(parameters["segment_ids"], dtype=tf.int32)
out = tf.math.segment_sum(data, segment_ids)
exit(([data], [out]))
