# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/irfft2d.py
rfft_length = []
rfft_length.append(parameters["input_shape"][-2])
rfft_length.append((parameters["input_shape"][-1] - 1) * 2)
rfft_input = create_tensor_data(np.float32, parameters["input_shape"])
rfft_result = np.fft.rfft2(rfft_input, rfft_length)

exit(([rfft_result], sess.run(
    outputs, feed_dict=dict(zip(inputs, [rfft_result])))))
