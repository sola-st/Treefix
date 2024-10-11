# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/scatter_nd.py
indices = np.array(parameters["indices_value"])
updates = create_tensor_data(parameters["updates_dtype"],
                             parameters["updates_shape"])
shape = np.array(parameters["shape_value"])
exit(([indices, updates, shape], sess.run(
    outputs, feed_dict=dict(zip(inputs, [indices, updates, shape])))))
