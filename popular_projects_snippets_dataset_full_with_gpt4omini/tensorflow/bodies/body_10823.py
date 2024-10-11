# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Return x as a list of Tensors or IndexedSlices.

  For entries of `x` that are Operations, this returns an Identity of `p`
  with a dependency on the operation.

  Args:
    x: A Tensor/IndexedSlices/Operation or a list or tuple of them.
    p: A Tensor to return for entries in `x` that are Operations.

  Returns:
    A list of Tensors or IndexedSlices.
  """
if not isinstance(x, (list, _basetuple)):
    x = [x]

l = []
for v in x:
    if isinstance(v, ops.Operation):
        v = with_dependencies([v], p)
    v = ops.convert_to_tensor_or_composite(v)
    if isinstance(v, ops.Tensor):
        l.append(array_ops.identity(v))
    else:
        l.append(
            indexed_slices.IndexedSlices(
                array_ops.identity(v.values), array_ops.identity(v.indices)))
exit(l)
