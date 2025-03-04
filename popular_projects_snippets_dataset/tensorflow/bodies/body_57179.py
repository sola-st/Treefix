# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/prelu.py
"""Make a set of tests to do PReLU."""

test_parameters = [
    {
        # The canonical case for image processing is having a 4D `input`
        # (NHWC)and `shared_axes`=[1, 2], so the alpha parameter is per
        # channel.
        "input_shape": [[1, 10, 10, 3], [3, 3, 3, 3]],
        "shared_axes": [[1, 2], [1]],
        "fully_quantize": [False],
        "input_range": [(-10, 10)],
    },
    {
        # 2D-3D example. Share the 2nd axis.
        "input_shape": [[20, 20], [20, 20, 20]],
        "shared_axes": [[1]],
        "fully_quantize": [False],
        "input_range": [(-10, 10)],
    },
    # Quantized cases.
    {
        # The canonical case for image processing is having a 4D `input`
        # (NHWC)and `shared_axes`=[1, 2], so the alpha parameter is per
        # channel.
        "input_shape": [[1, 10, 10, 3], [3, 3, 3, 3]],
        "shared_axes": [[1, 2], [1]],
        "fully_quantize": [True],
        "input_range": [(-10, 10)],
    },
    {
        # 2D-3D example. Share the 2nd axis.
        "input_shape": [[20, 20], [20, 20, 20]],
        "shared_axes": [[1]],
        "fully_quantize": [True],
        "input_range": [(-10, 10)],
    },
]

def build_graph(parameters):
    """Build the graph for the test case."""

    input_tensor = tf.compat.v1.placeholder(
        dtype=tf.float32, name="input", shape=parameters["input_shape"])
    prelu = tf.keras.layers.PReLU(shared_axes=parameters["shared_axes"])
    out = prelu(input_tensor)
    exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    """Build the inputs for the test case."""

    input_shape = parameters["input_shape"]
    input_values = create_tensor_data(
        np.float32, input_shape, min_value=-10, max_value=10)
    shared_axes = parameters["shared_axes"]

    alpha_shape = []
    for dim in range(1, len(input_shape)):
        alpha_shape.append(1 if dim in shared_axes else input_shape[dim])

    alpha_values = create_tensor_data(
        np.float32, alpha_shape, min_value=-5, max_value=5)

    # There should be only 1 trainable variable tensor.
    variables = tf.compat.v1.all_variables()
    assert len(variables) == 1
    sess.run(variables[0].assign(alpha_values))

    exit(([input_values], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_values])))))

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    use_frozen_graph=True)
