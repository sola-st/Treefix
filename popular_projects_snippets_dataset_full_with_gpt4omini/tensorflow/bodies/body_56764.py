# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/tensor_list_resize.py
"""Build the TensorListResize op testing graph."""
data = tf.compat.v1.placeholder(
    dtype=parameters["element_dtype"],
    shape=[parameters["num_elements"]] + parameters["element_shape"])
tensor_list = list_ops.tensor_list_from_tensor(data,
                                               parameters["element_shape"])
tensor_list = list_ops.tensor_list_resize(tensor_list,
                                          parameters["new_size"])
out = list_ops.tensor_list_stack(
    tensor_list, element_dtype=parameters["element_dtype"])
exit(([data], [out]))
