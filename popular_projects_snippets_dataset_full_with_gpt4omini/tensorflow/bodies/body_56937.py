# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/gather_nd.py
"""Make a set of tests to do gather_nd."""

test_parameters = [
    {
        "params_dtype": [tf.float32, tf.int32, tf.int64, tf.string],
        "params_shape": [[5, 1]],
        "indices_dtype": [tf.int32, tf.int64],
        "indices_shape": [[1, 1]],
    },
    {
        "params_dtype": [tf.float32, tf.int32, tf.int64, tf.string],
        "params_shape": [[5, 5]],
        "indices_dtype": [tf.int32, tf.int64],
        "indices_shape": [[2, 1], [2, 2]],
    },
    {
        "params_dtype": [tf.float32, tf.int32, tf.int64, tf.string],
        "params_shape": [[5, 5, 10]],
        "indices_dtype": [tf.int32, tf.int64],
        "indices_shape": [[3, 1], [2, 2], [2, 3], [2, 1, 3]],
    },
    {
        "params_dtype": [tf.float32, tf.string],
        "params_shape": [[1, 0]],
        "indices_dtype": [tf.int64],
        "indices_shape": [[0, 2]],
    },
]

def build_graph(parameters):
    """Build the gather_nd op testing graph."""
    params = tf.compat.v1.placeholder(
        dtype=parameters["params_dtype"],
        name="params",
        shape=parameters["params_shape"])
    indices = tf.compat.v1.placeholder(
        dtype=parameters["indices_dtype"],
        name="indices",
        shape=parameters["indices_shape"])
    out = tf.gather_nd(params, indices)
    exit(([params, indices], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    params = create_tensor_data(parameters["params_dtype"],
                                parameters["params_shape"])
    indices = create_tensor_data(parameters["indices_dtype"],
                                 parameters["indices_shape"], 0,
                                 parameters["params_shape"][0] - 1)
    exit(([params, indices], sess.run(
        outputs, feed_dict=dict(zip(inputs, [params, indices])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
