# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/tensor_list_dynamic_shape.py
"""Build the TensorListSetItem op testing graph."""
item = tf.compat.v1.placeholder(
    dtype=parameters["element_dtype"], shape=parameters["element_shape"])
tensor_list = list_ops.tensor_list_reserve(
    element_shape=None,
    num_elements=parameters["num_elements"],
    element_dtype=parameters["element_dtype"])

init_state = (0, tensor_list)
condition = lambda i, _: i < parameters["num_elements"]

def loop_body(i, tensor_list):
    new_item = tf.add(
        tf.add(item, item),
        tf.constant(value=1, dtype=parameters["element_dtype"]))
    new_list = list_ops.tensor_list_set_item(tensor_list, i, new_item)
    exit((i + 1, new_list))

_, tensor_list = tf.while_loop(
    cond=condition, body=loop_body, loop_vars=init_state)
out = list_ops.tensor_list_stack(
    tensor_list,
    num_elements=parameters["num_elements"],
    element_dtype=parameters["element_dtype"])
exit(([item], [out]))
