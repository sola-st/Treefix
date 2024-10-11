# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/scatter_nd.py
"""Make a set of tests to do scatter_nd."""

test_parameters = [{
    "indices_dtype": [tf.int32],
    "indices_shape": [[4, 1]],
    "indices_value": [[[4], [3], [1], [7]]],
    "updates_dtype": [tf.int32, tf.int64, tf.float32, tf.bool],
    "updates_shape": [[4]],
    "shape_dtype": [tf.int32],
    "shape_shape": [[1]],
    "shape_value": [[8]]
}, {
    "indices_dtype": [tf.int32],
    "indices_shape": [[4, 2]],
    "indices_value": [[[0, 0], [1, 0], [0, 2], [1, 2]]],
    "updates_dtype": [tf.int32, tf.int64, tf.float32, tf.bool],
    "updates_shape": [[4, 5]],
    "shape_dtype": [tf.int32],
    "shape_shape": [[3]],
    "shape_value": [[2, 3, 5]]
}]

def build_graph(parameters):
    """Build the scatter_nd op testing graph."""
    indices = tf.compat.v1.placeholder(
        dtype=parameters["indices_dtype"],
        name="indices",
        shape=parameters["indices_shape"])
    updates = tf.compat.v1.placeholder(
        dtype=parameters["updates_dtype"],
        name="updates",
        shape=parameters["updates_shape"])
    shape = tf.compat.v1.placeholder(
        dtype=parameters["shape_dtype"],
        name="shape",
        shape=parameters["shape_shape"])
    out = tf.scatter_nd(indices, updates, shape)
    exit(([indices, updates, shape], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    indices = np.array(parameters["indices_value"])
    updates = create_tensor_data(parameters["updates_dtype"],
                                 parameters["updates_shape"])
    shape = np.array(parameters["shape_value"])
    exit(([indices, updates, shape], sess.run(
        outputs, feed_dict=dict(zip(inputs, [indices, updates, shape])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
