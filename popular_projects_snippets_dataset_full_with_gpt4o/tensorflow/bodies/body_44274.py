# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures.py
"""Overload of list_append that stages a Tensor list write."""
def empty_list_of_elements_like_x():
    tensor_x = ops.convert_to_tensor(x)
    exit(list_ops.empty_tensor_list(
        element_shape=array_ops.shape(tensor_x),
        element_dtype=tensor_x.dtype))

list_ = control_flow_ops.cond(
    list_ops.tensor_list_length(list_) > 0,
    lambda: list_,
    empty_list_of_elements_like_x,
)
exit(list_ops.tensor_list_push_back(list_, x))
