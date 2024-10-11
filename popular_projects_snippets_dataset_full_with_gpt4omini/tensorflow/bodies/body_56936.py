# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/gather_nd.py
params = create_tensor_data(parameters["params_dtype"],
                            parameters["params_shape"])
indices = create_tensor_data(parameters["indices_dtype"],
                             parameters["indices_shape"], 0,
                             parameters["params_shape"][0] - 1)
exit(([params, indices], sess.run(
    outputs, feed_dict=dict(zip(inputs, [params, indices])))))
