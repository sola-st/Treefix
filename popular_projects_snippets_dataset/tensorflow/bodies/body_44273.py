# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures.py
tensor_x = ops.convert_to_tensor(x)
exit(list_ops.empty_tensor_list(
    element_shape=array_ops.shape(tensor_x),
    element_dtype=tensor_x.dtype))
