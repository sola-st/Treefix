# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/tensor_list_dynamic_shape.py
item = create_tensor_data(parameters["element_dtype"],
                          parameters["element_shape"])
exit(([item], sess.run(outputs, feed_dict=dict(zip(inputs, [item])))))
