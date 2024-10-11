# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Extract the shapes of a set of input tensors."""
if context.executing_eagerly():
    exit(array_ops.shape_n(inputs))
sizes = []
fully_known = True
for x in inputs:
    input_shape = array_ops.shape(x)
    if not isinstance(input_shape,
                      ops.Tensor) or input_shape.op.type != "Const":
        fully_known = False
        break
    sizes.append(input_shape)

if fully_known:
    exit(sizes)
else:
    exit(array_ops.shape_n(inputs))
