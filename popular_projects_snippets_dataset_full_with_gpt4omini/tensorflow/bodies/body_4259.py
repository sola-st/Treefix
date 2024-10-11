# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/d_checkpoint.py
"""Saves the saveable objects to a checkpoint with `file_prefix`.

    Also query the generated shards from the distributed DTensor SaveV2 ops and
    do a MergeV2 on those. Each op here is backed by a global_barrier to avoid
    racing from multiple clients.

    Args:
      file_prefix: A string or scalar string Tensor containing the prefix to
        save under.
      options: Optional `CheckpointOptions` object. This is unused in DTensor.

    Returns:
      An `Operation`, or None when executing eagerly.
    """
if options is not None and options.experimental_io_device is not None:
    raise ValueError(
        "Specified experimental_io_device in DTensor checkpoint is not supported."
    )
del options
tensor_names = []
tensors = []
tensor_slices = []
for saveable in self._saveable_objects:
    for spec in saveable.specs:
        tensor = spec.tensor
        # A tensor value of `None` indicates that this SaveableObject gets
        # recorded in the object graph, but that no value is saved in the
        # checkpoint.
        if tensor is not None:
            if api.device_name() != spec.device:
                # Some small tensors are placed on CPU0 from save manager and
                # broadcasted to DTensor mesh, e,g., SaveCounter.
                tensor = api.pack([tensor] *
                                  self._mesh.host_mesh().num_local_devices(),
                                  layout.Layout.replicated(
                                      self._mesh.host_mesh(),
                                      rank=tensor.shape.rank))
            tensor_names.append(spec.name)
            tensors.append(tensor)
            tensor_slices.append(spec.slice_spec)
exit(save_restore.sharded_save(self._mesh, file_prefix, tensor_names,
                                 tensor_slices, tensors))
