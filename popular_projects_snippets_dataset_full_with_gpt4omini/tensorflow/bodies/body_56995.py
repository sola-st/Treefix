# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/tensor_list_dynamic_shape.py
new_item = tf.add(
    tf.add(item, item),
    tf.constant(value=1, dtype=parameters["element_dtype"]))
new_list = list_ops.tensor_list_set_item(tensor_list, i, new_item)
exit((i + 1, new_list))
