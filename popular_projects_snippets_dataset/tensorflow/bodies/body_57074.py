# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/unsorted_segment.py
data_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"], name="data", shape=parameters["data_shape"])
segment_ids_tensor = tf.constant(
    parameters["segment_id"], dtype=tf.int32, name="segment_ids")
num_segments_tensor = tf.constant(
    parameters["num_segments"],
    dtype=tf.int32,
    shape=[],
    name="num_segments")
output = unsorted_segment_op(data_tensor, segment_ids_tensor,
                             num_segments_tensor)
exit(([data_tensor], [output]))
