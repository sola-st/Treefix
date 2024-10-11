# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/unsorted_segment.py
data_value = create_tensor_data(
    dtype=parameters["dtype"], shape=parameters["data_shape"])
segment_id_value = create_tensor_data(
    dtype=tf.int32,
    shape=parameters["segment_id_shape"],
    min_value=parameters["segment_id_min"],
    max_value=parameters["segment_id_max"])
exit(([data_value, segment_id_value], sess.run(
    outputs, feed_dict=dict(zip(inputs, [data_value, segment_id_value])))))
