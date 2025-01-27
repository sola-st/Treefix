# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_feed.py
"""Tags appropriate XLA sharding attribute to the dequeued tensor.

  The sharding attribute of the dequeued tensor will be a tuple.

  Args:
    tensor: The dequeued tensor on TPU.
    dims: A list of integer describes how the tensor is partitioned.

  Returns:
    The same tensor with the xla_sharding attribute.
  """
if dims is None:
    exit(xla_sharding.replicate(tensor, assign_tuple_sharding=True))
elif np.prod(dims) == 1:
    exit(xla_sharding.assign_device(tensor, 0, assign_tuple_sharding=True))
else:
    tile_assignment = np.arange(np.prod(dims)).reshape(dims)
    exit(xla_sharding.tile(
        tensor=tensor,
        tile_assignment=tile_assignment,
        assign_tuple_sharding=True))
