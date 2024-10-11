# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/unsorted_segment.py
"""Make a set of tests for given unsorted_segment op."""
test_parameters = [{
    "data_shape": [[5]],
    "segment_id": [[0, 1, 1, 0, 1]],
    "num_segments": [2],
    "dtype": [tf.int32, tf.float32],
    "multi_node": [0]
}, {
    "data_shape": [[2, 3, 4], [2, 5, 2]],
    "segment_id": [[0, 1]],
    "num_segments": [2],
    "dtype": [tf.int32, tf.float32],
    "multi_node": [0]
}, {
    "data_shape": [[4]],
    "segment_id": [[0, 0, 1, 8]],
    "num_segments": [9],
    "dtype": [tf.int32, tf.float32],
    "multi_node": [0]
}, {
    "data_shape": [[3]],
    "segment_id": [[-1, -2, -1]],
    "num_segments": [1],
    "dtype": [tf.int32, tf.float32],
    "multi_node": [0]
}, {
    "data_shape": [[3]],
    "segment_id": [[-1, 0, 1]],
    "num_segments": [2],
    "dtype": [tf.int32, tf.float32],
    "multi_node": [0]
}, {
    "data_shape": [[3, 2]],
    "segment_id": [[-1, 0, 0]],
    "num_segments": [1],
    "dtype": [tf.int32, tf.float32],
    "multi_node": [0]
}, {
    "data_shape": [[3, 2]],
    "segment_id": [[-1, -2, -1]],
    "num_segments": [1],
    "dtype": [tf.int32, tf.float32],
    "multi_node": [0]
}, {
    "data_shape": [[4]],
    "segment_id_shape": [[4]],
    "segment_id_min": [0],
    "segment_id_max": [1],
    "num_segments": [2],
    "dtype": [tf.int32, tf.float32],
    "segment_id_2": [[0, 0]],
    "num_segments_2": [1],
    "multi_node": [1]
}, {
    "data_shape": [[2, 2, 3]],
    "segment_id": [[[1, 2], [3, 4]], [4, 5],
                   [[[1, 2, 3], [3, 4, 5]], [[1, 2, 4], [0, 0, -1]]]],
    "num_segments": [10],
    "dtype": [tf.int32, tf.float32],
    "multi_node": [0]
}, {
    "data_shape": [[2, 0, 3]],
    "segment_id": [[1, 1]],
    "num_segments": [2],
    "dtype": [tf.int32, tf.float32],
    "multi_node": [0]
}]

def build_graph_one_node(parameters):
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


# test cases for handling dynamically shaped input tensor
def build_graph_multi_node(parameters):
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

def build_graph(parameters):
    multi_node = parameters["multi_node"]
    if multi_node:
        exit(build_graph_multi_node(parameters))

    exit(build_graph_one_node(parameters))

def build_inputs_one_node(parameters, sess, inputs, outputs):
    data_value = create_tensor_data(
        parameters["dtype"], shape=parameters["data_shape"])
    exit(([data_value], sess.run(
        outputs, feed_dict=dict(zip(inputs, [data_value])))))

def build_inputs_multi_node(parameters, sess, inputs, outputs):
    data_value = create_tensor_data(
        dtype=parameters["dtype"], shape=parameters["data_shape"])
    segment_id_value = create_tensor_data(
        dtype=tf.int32,
        shape=parameters["segment_id_shape"],
        min_value=parameters["segment_id_min"],
        max_value=parameters["segment_id_max"])
    exit(([data_value, segment_id_value], sess.run(
        outputs, feed_dict=dict(zip(inputs, [data_value, segment_id_value])))))

def build_inputs(parameters, sess, inputs, outputs):
    multi_node = parameters["multi_node"]
    if multi_node:
        exit(build_inputs_multi_node(parameters, sess, inputs, outputs))

    exit(build_inputs_one_node(parameters, sess, inputs, outputs))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
