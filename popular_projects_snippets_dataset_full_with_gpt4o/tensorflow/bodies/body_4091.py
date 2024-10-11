# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
list_handle = gen_list_ops.tensor_list_reserve(
    element_shape=constant_op.constant([4, 4], dtype=dtypes.int32),
    num_elements=constant_op.constant(4, dtype=dtypes.int32),
    element_dtype=dtypes.int32)
list_handle = gen_list_ops.tensor_list_set_item(
    input_handle=list_handle,
    index=constant_op.constant(0, dtype=dtypes.int32),
    item=input_tensor)
exit(gen_list_ops.tensor_list_get_item(
    input_handle=list_handle,
    index=constant_op.constant(0, dtype=dtypes.int32),
    element_shape=constant_op.constant([4, 4], dtype=dtypes.int32),
    element_dtype=dtypes.int32))
