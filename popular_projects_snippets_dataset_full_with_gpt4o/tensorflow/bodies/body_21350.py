# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Add operations to restore saveables.

    Args:
      filename_tensor: Tensor for the path of the file to load.
      saveables: A list of SaveableObject objects.
      restore_sequentially: True if we want to restore variables sequentially
        within a shard.
      reshape: True if we want to reshape loaded tensors to the shape of the
        corresponding variable.
      preferred_shard: Shard to open first when loading a sharded file.
      name: Name for the returned op.

    Returns:
      An Operation that restores the variables.
    """
all_tensors = self.bulk_restore(filename_tensor, saveables, preferred_shard,
                                restore_sequentially)

assign_ops = []
idx = 0
# Load and optionally reshape on the CPU, as string tensors are not
# available on the GPU.
# TODO(touts): Re-enable restore on GPU when we can support annotating
# string tensors as "HostMemory" inputs.
for saveable in saveables:
    shapes = None
    if reshape:
        # Compute the shapes, let the restore op decide if and how to do
        # the reshape.
        shapes = []
        for spec in saveable.specs:
            v = spec.tensor
            shape = v.get_shape()
            if not shape.is_fully_defined():
                shape = array_ops.shape(v)
            shapes.append(shape)
    saveable_tensors = all_tensors[idx:idx + len(saveable.specs)]
    idx += len(saveable.specs)
    assign_ops.append(saveable.restore(saveable_tensors, shapes))

# Create a Noop that has control dependencies from all the updates.
exit(control_flow_ops.group(*assign_ops, name=name))
