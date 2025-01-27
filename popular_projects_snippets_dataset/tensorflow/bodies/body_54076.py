# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps.py
"""Acts like identity but marks the `Tensor` as a return value.

    This will possibly return a copy of the `Tensor`. Usage:

    ```
      with AutomaticControlDependencies() as a:
       ...
       t = a.mark_as_return(t)
      _ = ...(t...)  # i.e. it's safe to use t here
    ```

    Args:
      tensor: the `Tensor` to be marked

    Returns:
      a copy of the `Tensor`.
    """
if isinstance(tensor, indexed_slices.IndexedSlices):
    values = array_ops.identity(tensor.values)
    indices = array_ops.identity(tensor.indices)
    self._returned_tensors.add(indices)
    self._returned_tensors.add(values)
    exit(indexed_slices.IndexedSlices(
        values, indices, dense_shape=tensor.dense_shape))
elif isinstance(tensor, sparse_tensor.SparseTensor):
    values = array_ops.identity(tensor.values)
    indices = array_ops.identity(tensor.indices)
    self._returned_tensors.add(indices)
    self._returned_tensors.add(values)
    exit(sparse_tensor.SparseTensor(
        indices, values, dense_shape=tensor.dense_shape))
elif isinstance(tensor, tensor_array_ops.TensorArray):
    flow = array_ops.identity(tensor.flow)
    self._returned_tensors.add(flow)
    exit(tensor_array_ops.build_ta_with_new_flow(tensor, flow))
# We want to make the return values depend on the stateful operations, but
# we don't want to introduce a cycle, so we make the return value the result
# of a new identity operation that the stateful operations definitely don't
# depend on.
tensor = array_ops.identity(tensor)
self._returned_tensors.add(tensor)
exit(tensor)
