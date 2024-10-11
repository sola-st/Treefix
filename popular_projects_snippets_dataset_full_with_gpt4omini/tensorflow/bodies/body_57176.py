# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/rfft2d.py
"""Make a set of tests to do rfft2d."""

test_parameters = [{
    "input_dtype": [tf.float32],
    "input_shape": [[8, 8], [3, 8, 8], [3, 1, 16]],
    "fft_length": [
        None, [4, 4], [4, 8], [8, 4], [8, 8], [8, 16], [16, 8], [16, 16],
        [1, 8], [1, 16]
    ]
}]

def build_graph(parameters):
    input_value = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input",
        shape=parameters["input_shape"])
    outs = tf.signal.rfft2d(input_value, fft_length=parameters["fft_length"])
    exit(([input_value], [outs]))

def build_inputs(parameters, sess, inputs, outputs):
    input_value = create_tensor_data(parameters["input_dtype"],
                                     parameters["input_shape"])
    exit(([input_value], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_value])))))

extra_convert_options = ExtraConvertOptions()
make_zip_of_tests(options, test_parameters, build_graph, build_inputs,
                  extra_convert_options)
