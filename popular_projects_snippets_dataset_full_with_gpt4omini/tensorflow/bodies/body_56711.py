# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/embedding_lookup.py
params = create_tensor_data(parameters["params_dtype"],
                            parameters["params_shape"])
ids = create_tensor_data(parameters["ids_dtype"], parameters["ids_shape"],
                         0, parameters["params_shape"][0] - 1)
exit(([params, ids], sess.run(
    outputs, feed_dict=dict(zip(inputs, [params, ids])))))
