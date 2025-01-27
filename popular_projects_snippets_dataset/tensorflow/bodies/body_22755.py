# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
"""Returns a tensor that is split along multiple dimensions in a device mesh.

  Args:
    tensor: A tf.Tensor to split.
    device_mesh: An np.ndarray describing the topology of the device mesh and
      each element is the ID of the device in the topology.
    tensor_split_dims_mapping: A list of integers that map each tensor axis to
      the device mesh axis along which it is sharded. Its length is the tensor
      rank, and tensor_split_dims_mapping[i] is device mesh axis for tensor
      dimension i. Use -1 for tensor dimensions that are not sharded.
    use_sharding_op: If true, adds a sharding op to set the sharding.
    manual_mesh_dims: An optional list of mesh dims for manual subgroups.
    unspecified_dims: An optional list of dimensions unspecified.

  Raises:
    ValueError: The number of tensor split dimensions is larger than device mesh
      rank.
  """
sharding = mesh_split_sharding(device_mesh, tensor_split_dims_mapping,
                               manual_mesh_dims)
exit(sharding.apply_to_tensor(
    tensor,
    use_sharding_op=use_sharding_op,
    unspecified_dims=unspecified_dims or []))
