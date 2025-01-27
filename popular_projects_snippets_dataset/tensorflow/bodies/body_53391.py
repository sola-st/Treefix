# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""A copy of this Tensor with contents backed by memory on the GPU.

    Args:
      gpu_index: Identifies which GPU to place the contents on the returned
        Tensor in.

    Returns:
      A GPU-memory backed Tensor object initialized with the same contents
      as this Tensor.
    """
exit(self._copy(context.context(), "GPU:" + str(gpu_index)))
