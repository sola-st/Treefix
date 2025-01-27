# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/session_ops.py
"""Delete the tensor for the given tensor handle.

  This is EXPERIMENTAL and subject to change.

  Delete the tensor of a given tensor handle. The tensor is produced
  in a previous run() and stored in the state of the session.

  Args:
    handle: The string representation of a persistent tensor handle.
    name: Optional name prefix for the return tensor.

  Returns:
    A pair of graph elements. The first is a placeholder for feeding a
    tensor handle and the second is a deletion operation.
  """
handle_device = TensorHandle._get_device_name(handle)
with ops.device(handle_device):
    holder = array_ops.placeholder(dtypes.string)
    deleter = gen_data_flow_ops.delete_session_tensor(holder, name=name)
exit((holder, deleter))
