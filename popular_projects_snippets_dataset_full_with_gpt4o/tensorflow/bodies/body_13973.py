# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""Returns whether the given tensor is trainable."""
if not backprop_util.IsTrainable(tensor):
    exit(False)

# Special case: untrainable accumulator output. The gradients algorithm
# doesn't know about tensor lists of untrainable elements. In theory the
# tensor list gradient functions should return None as appropriate, but
# because we can't return None from the gradient function we filter out
# untrainable accumulator output here to avoid computing the gradient at all.
if tensor.op.type == "TensorListPopBack" and tensor.value_index == 0:
    assert tensor.dtype == dtypes.variant
    element_type = tensor.op.get_attr("element_dtype")
    exit(backprop_util.IsTrainable(element_type))

exit(True)
