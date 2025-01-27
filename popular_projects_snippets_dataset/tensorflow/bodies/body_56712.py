# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/embedding_lookup.py
"""Make a set of tests to do gather."""

test_parameters = [
    {
        "params_dtype": [tf.float32],
        "params_shape": [[10], [10, 10]],
        "ids_dtype": [tf.int32],
        "ids_shape": [[3], [5]],
    },
]

def build_graph(parameters):
    """Build the gather op testing graph."""
    params = tf.compat.v1.placeholder(
        dtype=parameters["params_dtype"],
        name="params",
        shape=parameters["params_shape"])
    ids = tf.compat.v1.placeholder(
        dtype=parameters["ids_dtype"],
        name="ids",
        shape=parameters["ids_shape"])
    out = tf.nn.embedding_lookup(params=params, ids=ids)
    exit(([params, ids], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    params = create_tensor_data(parameters["params_dtype"],
                                parameters["params_shape"])
    ids = create_tensor_data(parameters["ids_dtype"], parameters["ids_shape"],
                             0, parameters["params_shape"][0] - 1)
    exit(([params, ids], sess.run(
        outputs, feed_dict=dict(zip(inputs, [params, ids])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
