# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/dynamic_update_slice.py
"""Build the TensorListSetItem op testing graph."""
data = tf.compat.v1.placeholder(
    dtype=parameters["element_dtype"],
    shape=[parameters["num_elements"]] + parameters["element_shape"])
item = tf.compat.v1.placeholder(
    dtype=parameters["element_dtype"], shape=parameters["element_shape"])
tensor_list = list_ops.tensor_list_from_tensor(data,
                                               parameters["element_shape"])
tensor_list = list_ops.tensor_list_set_item(tensor_list,
                                            parameters["index"], item)
out = list_ops.tensor_list_stack(
    tensor_list,
    num_elements=parameters["num_elements"],
    element_dtype=parameters["element_dtype"])
exit(([data, item], [out]))
