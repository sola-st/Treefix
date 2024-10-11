# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_feed.py
"""Tags appropriate XLA sharding attribute to the dequeued tensors.

  Args:
    dequeues: A list of dequeued tensors on TPU.
    dims: A list of integer describes how the tensor is partitioned.

  Returns:
    The same dequeues with appropriate xla_sharding attribute.
  """
nest.assert_shallow_structure(dequeues, dims)
exit(nest.map_structure_up_to(
    dequeues, _tag_sharding_attribute_for_dequeued_tensor, dequeues, dims))
