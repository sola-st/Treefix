# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/l2norm_shared_epsilon.py
"""Regression test for a bug (b/122651451)."""

# Chose a set of parameters
test_parameters = [{
    "input_shape": [[5, 7]],
    "dim": [1],
    "epsilon": [1e-8],
}]

def build_graph(parameters):
    input_tensor = tf.compat.v1.placeholder(
        dtype=tf.float32, name="input", shape=parameters["input_shape"])
    epsilon = tf.constant(parameters["epsilon"])
    out1 = tf.nn.l2_normalize(input_tensor, parameters["dim"], epsilon=epsilon)
    out2 = tf.nn.l2_normalize(input_tensor, parameters["dim"], epsilon=epsilon)
    out = out1 + out2
    exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_values = create_tensor_data(
        np.float32, parameters["input_shape"], min_value=-4, max_value=10)
    exit(([input_values], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_values])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
