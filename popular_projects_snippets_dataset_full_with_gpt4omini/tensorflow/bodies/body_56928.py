# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/tensor_list_get_item.py
"""Build the TensorListGetItem op testing graph."""
data = tf.compat.v1.placeholder(
    dtype=parameters["element_dtype"],
    shape=[parameters["num_elements"]] + parameters["element_shape"])
tensor_list = list_ops.tensor_list_from_tensor(data,
                                               parameters["element_shape"])
out = list_ops.tensor_list_get_item(tensor_list, parameters["index"],
                                    parameters["element_dtype"])
exit(([data], [out]))
