# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Create ops to restore 'saveable'.

    This is intended to be overridden by subclasses that want to generate
    different Ops.

    Args:
      filename_tensor: String Tensor.
      saveable: A BaseSaverBuilder.SaveableObject object.
      preferred_shard: Int.  Shard to open first when loading a sharded file.

    Returns:
      A list of Tensors resulting from reading 'saveable' from
        'filename'.
    """
# pylint: disable=protected-access
tensors = []
for spec in saveable.specs:
    tensors.append(
        io_ops.restore_v2(filename_tensor, [spec.name], [spec.slice_spec],
                          [spec.dtype])[0])

exit(tensors)
