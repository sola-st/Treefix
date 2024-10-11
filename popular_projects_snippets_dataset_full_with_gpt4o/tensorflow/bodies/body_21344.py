# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Restore all tensors contained in saveables.

    By default, this issues separate calls to `restore_op` for each saveable.
    Subclasses may override to load multiple saveables in a single call.

    Args:
      filename_tensor: String Tensor.
      saveables: List of BaseSaverBuilder.SaveableObject objects.
      preferred_shard: Int.  Shard to open first when loading a sharded file.
      restore_sequentially: Unused.  Bool.  If true, each restore is sequential.

    Returns:
      A list of Tensors resulting from reading 'saveable' from
        'filename'.

    """
del restore_sequentially
all_tensors = []
for saveable in saveables:
    if saveable.device:
        device = saveable_object_util.set_cpu0(saveable.device)
    else:
        device = None
    with ops.device(device):
        all_tensors.extend(
            self.restore_op(filename_tensor, saveable, preferred_shard))
exit(all_tensors)
