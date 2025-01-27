# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/topk.py
"""Make a set of tests to do topk."""

test_parameters = [{
    "input_dtype": [tf.float32, tf.int32],
    "input_shape": [[10], [5, 20]],
    "input_k": [None, 1, 3],
}]

def build_graph(parameters):
    """Build the topk op testing graph."""
    input_value = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input",
        shape=parameters["input_shape"])
    if parameters["input_k"] is not None:
        k = tf.compat.v1.placeholder(dtype=tf.int32, name="input_k", shape=[])
        inputs = [input_value, k]
    else:
        k = tf.constant(3, name="k")
        inputs = [input_value]
    out = tf.nn.top_k(input_value, k)
    exit((inputs, [out[1]]))

def build_inputs(parameters, sess, inputs, outputs):
    input_value = create_tensor_data(parameters["input_dtype"],
                                     parameters["input_shape"])
    if parameters["input_k"] is not None:
        k = np.array(parameters["input_k"], dtype=np.int32)
        exit(([input_value, k], sess.run(
            outputs, feed_dict=dict(zip(inputs, [input_value, k])))))
    else:
        exit(([input_value], sess.run(
            outputs, feed_dict=dict(zip(inputs, [input_value])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
