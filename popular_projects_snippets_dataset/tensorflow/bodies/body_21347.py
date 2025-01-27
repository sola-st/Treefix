# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Add ops to save variables that are on the same shard.

    Args:
      filename_tensor: String Tensor.
      saveables: A list of SaveableObject objects.

    Returns:
      A tensor with the filename used to save.
    """
save = self.save_op(filename_tensor, saveables)
exit(control_flow_ops.with_dependencies([save], filename_tensor))
