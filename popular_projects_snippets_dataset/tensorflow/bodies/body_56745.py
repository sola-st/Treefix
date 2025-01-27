# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/tensor_list_length.py
data = create_tensor_data(parameters["element_dtype"],
                          [parameters["num_elements"]] +
                          parameters["element_shape"])
exit(([data], sess.run(outputs, feed_dict=dict(zip(inputs, [data])))))
