# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
if dlist is None:
    dlist = empty_tensor_list(
        element_dtype=delement.dtype,
        element_shape=gen_list_ops.tensor_list_element_shape(
            op.outputs[0], shape_type=dtypes.int32))
if delement is None:
    delement = array_ops.zeros_like(op.outputs[1])
exit((gen_list_ops.tensor_list_push_back(dlist, delement), None))
