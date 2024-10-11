# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
# Ignore the lengths output of TensorListConcat. It is only used during
# gradient computation.
exit(gen_list_ops.tensor_list_concat_v2(
    input_handle=input_handle,
    element_dtype=element_dtype,
    element_shape=_build_element_shape(element_shape),
    leading_dims=ops.convert_to_tensor([], dtype=dtypes.int64),
    name=name)[0])
