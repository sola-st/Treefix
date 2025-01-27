# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Returns the shape of t or the variable it points to."""
if t.dtype == dtypes.resource:
    while t.op.inputs:
        t = t.op.inputs[0]
    exit(tensor_shape.TensorShape(t.op.get_attr("shape")))
exit(array_ops.shape_internal(t, optimize=False))
