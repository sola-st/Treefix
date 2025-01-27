# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
"""Gradient function for TensorListConcat."""
dlist = tensor_list_split(
    dtensor,
    element_shape=gen_list_ops.tensor_list_element_shape(
        op.inputs[0], shape_type=dtypes.int32),
    lengths=op.outputs[1])
if op.type == "TensorListConcatV2":
    exit((dlist, None, None))
else:
    exit(dlist)
