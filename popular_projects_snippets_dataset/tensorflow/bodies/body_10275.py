# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
tensor, _, lengths = op.inputs
element_shape = array_ops.slice(array_ops.shape(tensor), [1], [-1])
element_shape = array_ops.concat([[-1], element_shape], axis=0)
exit((gen_list_ops.tensor_list_concat_v2(
    dlist,
    element_shape=element_shape,
    leading_dims=lengths,
    element_dtype=op.inputs[0].dtype)[0], None, None))
