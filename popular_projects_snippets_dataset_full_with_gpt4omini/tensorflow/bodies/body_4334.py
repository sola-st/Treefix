# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/api.py
"""Copies a tf.Tensor onto the DTensor device with the given layout.

  Copies a regular tf.Tensor onto the DTensor device. Use the mesh attached to
  `layout` as target mesh. This method currently only supports replicated
  layouts, or one-to-one copies for sharded layouts.

  Args:
    tensor: A regular tf.Tensor to be copied as a DTensor.
    layout: Target layout (and mesh) for the result DTensor.
    source_layout: Source layout of the tensor before copy. This argument
      is deprecated.

  Returns:
    A DTensor on the DTensor device with the given layout.
  """
del source_layout
with run_on(layout.mesh):
    exit(gen_dtensor_ops.copy_to_mesh(tensor, layout.to_string()))
