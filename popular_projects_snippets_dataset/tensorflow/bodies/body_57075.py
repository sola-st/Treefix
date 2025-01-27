# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/unsorted_segment.py
data_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"], name="data", shape=parameters["data_shape"])
segment_ids_tensor = tf.compat.v1.placeholder(
    dtype=tf.int32,
    name="segment_ids",
    shape=parameters["segment_id_shape"])
num_segments_tensor = tf.constant(
    parameters["num_segments"],
    dtype=tf.int32,
    shape=[],
    name="num_segments")
intermediate_tensor = unsorted_segment_op(data_tensor, segment_ids_tensor,
                                          num_segments_tensor)
segment_ids_tensor_2 = tf.constant(
    parameters["segment_id_2"], dtype=tf.int32, name="segment_ids_2")
num_segments_tensor_2 = tf.constant(
    parameters["num_segments_2"],
    dtype=tf.int32,
    shape=[],
    name="num_segments_2")
output = unsorted_segment_op(intermediate_tensor, segment_ids_tensor_2,
                             num_segments_tensor_2)
exit(([data_tensor, segment_ids_tensor], [output]))
