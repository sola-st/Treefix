# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/resize_nearest_neighbor.py
"""Make a set of tests to do resize_nearest_neighbor."""

test_parameters = [{
    "dtype": [tf.float32],
    "input_shape": [[1, 3, 4, 3], [1, 10, 2, 1]],
    "size": [[1, 1], [4, 3], [2, 2], [5, 6]],
    "align_corners": [False],
    "half_pixel_centers": [False],
    "fully_quantize": [True, False],
}, {
    "dtype": [tf.float32],
    "input_shape": [[1, 16, 24, 3], [1, 12, 18, 3]],
    "size": [[8, 12], [12, 18]],
    "align_corners": [True],
    "half_pixel_centers": [False],
    "fully_quantize": [True, False]
}, {
    "dtype": [tf.float32],
    "input_shape": [[1, 16, 24, 3], [1, 12, 18, 3]],
    "size": [[8, 12], [12, 18]],
    "align_corners": [False],
    "half_pixel_centers": [True],
    "fully_quantize": [True, False]
}]

def build_graph(parameters):
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["dtype"],
        name="input",
        shape=parameters["input_shape"])
    out = tf.compat.v1.image.resize_nearest_neighbor(
        input_tensor,
        size=parameters["size"],
        align_corners=parameters["align_corners"],
        half_pixel_centers=parameters["half_pixel_centers"])
    exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_values = create_tensor_data(
        parameters["dtype"],
        parameters["input_shape"],
        min_value=-1,
        max_value=1)
    exit(([input_values], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_values])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
