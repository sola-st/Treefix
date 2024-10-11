# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/irfft2d.py
"""Make a set of tests to do irfft2d."""

test_parameters = [{
    "input_dtype": [tf.complex64],
    "input_shape": [[4, 3]],
    "fft_length": [[4, 4], [2, 2], [2, 4]]
}, {
    "input_dtype": [tf.complex64],
    "input_shape": [[3, 8, 5]],
    "fft_length": [[2, 4], [2, 8], [8, 8]]
}, {
    "input_dtype": [tf.complex64],
    "input_shape": [[3, 1, 9]],
    "fft_length": [[1, 8], [1, 16]]
}]

def build_graph(parameters):
    input_value = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input",
        shape=parameters["input_shape"])
    outs = tf.signal.irfft2d(input_value, fft_length=parameters["fft_length"])
    exit(([input_value], [outs]))

def build_inputs(parameters, sess, inputs, outputs):
    rfft_length = []
    rfft_length.append(parameters["input_shape"][-2])
    rfft_length.append((parameters["input_shape"][-1] - 1) * 2)
    rfft_input = create_tensor_data(np.float32, parameters["input_shape"])
    rfft_result = np.fft.rfft2(rfft_input, rfft_length)

    exit(([rfft_result], sess.run(
        outputs, feed_dict=dict(zip(inputs, [rfft_result])))))

extra_convert_options = ExtraConvertOptions()
extra_convert_options.allow_custom_ops = True
make_zip_of_tests(options, test_parameters, build_graph, build_inputs,
                  extra_convert_options)
