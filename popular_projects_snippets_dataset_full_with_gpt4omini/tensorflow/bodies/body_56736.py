# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/segment_sum.py
"""Make a set of tests to do segment_sum."""

test_parameters = [
    {
        "data_shape": [[4, 4], [4], [4, 3, 2]],
        "data_dtype": [tf.float32, tf.int32],
        "segment_ids": [[0, 0, 1, 1], [0, 1, 2, 2], [0, 1, 2, 3],
                        [0, 0, 0, 0]],
    },
]

def build_graph(parameters):
    """Build the segment_sum op testing graph."""
    data = tf.compat.v1.placeholder(
        dtype=parameters["data_dtype"],
        name="data",
        shape=parameters["data_shape"])
    segment_ids = tf.constant(parameters["segment_ids"], dtype=tf.int32)
    out = tf.math.segment_sum(data, segment_ids)
    exit(([data], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    data = create_tensor_data(parameters["data_dtype"],
                              parameters["data_shape"])
    exit(([data], sess.run(outputs, feed_dict=dict(zip(inputs, [data])))))

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    expected_tf_failures=0)
