# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/dynamic_update_slice.py
data = create_tensor_data(parameters["element_dtype"],
                          [parameters["num_elements"]] +
                          parameters["element_shape"])
item = create_tensor_data(parameters["element_dtype"],
                          parameters["element_shape"])
exit(([data, item], sess.run(
    outputs, feed_dict=dict(zip(inputs, [data, item])))))
