# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/sparse_to_dense.py
if parameters["value_is_scalar"] and parameters["value_count"] == 1:
    input_value = create_scalar_data(parameters["value_dtype"])
else:
    input_value = create_tensor_data(parameters["value_dtype"],
                                     [parameters["value_count"]])
exit(([input_value], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_value])))))
