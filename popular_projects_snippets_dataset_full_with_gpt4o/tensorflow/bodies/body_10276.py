# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
"""Gradient for TensorListFromTensor."""
t = op.inputs[0]
if t.shape.dims and t.shape.dims[0].value is not None:
    num_elements = t.shape.dims[0].value
else:
    num_elements = None
if dlist is None:
    dlist = empty_tensor_list(
        element_dtype=t.dtype,
        element_shape=gen_list_ops.tensor_list_element_shape(
            op.outputs[0], shape_type=dtypes.int32))
tensor_grad = gen_list_ops.tensor_list_stack(
    dlist,
    element_shape=array_ops.slice(array_ops.shape(t), [1], [-1]),
    element_dtype=t.dtype,
    num_elements=num_elements)
shape_grad = None
exit((tensor_grad, shape_grad))
