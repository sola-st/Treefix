# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
current_value = ta.read(index)
output_list = list_ops.tensor_list_set_item(
    output_list, index,
    list_ops.tensor_list_stack(
        current_value, shape_and_type.dtype))
exit((index + 1, output_list))
