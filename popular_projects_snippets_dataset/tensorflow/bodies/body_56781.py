# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/l2norm.py
"""Make a set of tests to do l2norm."""

# Chose a set of parameters
test_parameters = [{
    "input_shape": [[5, 7], [1, 1, 1, 1], [1, 3, 4, 3], [3, 15, 14, 3]],
    "dim": [0, 1, 2, 3, [2, 3], -2],
    "epsilon": [None, 1e-12, 1e-3],
    "fully_quantize": [False],
}, {
    "input_shape": [[1, 1, 1, 1], [1, 3, 4, 3], [3, 15, 14, 3]],
    "dim": [3],
    "epsilon": [None, 1e-12],
    "fully_quantize": [True],
}, {  # use another group of test so the dim is set to fuse to tfl.l2norm
    "input_shape": [[5, 7]],
    "dim": [1],
    "epsilon": [None, 1e-12],
    "fully_quantize": [True],
}]

def build_graph(parameters):
    input_tensor = tf.compat.v1.placeholder(
        dtype=tf.float32, name="input", shape=parameters["input_shape"])
    if parameters["epsilon"]:
        out = tf.nn.l2_normalize(
            input_tensor, parameters["dim"], epsilon=parameters["epsilon"])
    else:
        out = tf.nn.l2_normalize(input_tensor, parameters["dim"])
    exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_values = create_tensor_data(
        np.float32, parameters["input_shape"], min_value=-1, max_value=1)
    exit(([input_values], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_values])))))

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    expected_tf_failures=9)
