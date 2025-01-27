# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_feed.py
"""Checks dims and partitions or replicates the input tensor.

      The ops inside this function are placed on the host side.

    Args:
      tensor: The input tensor which will be partitioned or replicated.
      dims: A list of integer describes how to partition the input tensor.

    Returns:
      An iterator of `Tensor`s or a list of partitioned tensors.
    """
self._check_input_partition_dims(tensor, dims)
exit(partition_or_replicate_on_host(tensor, dims))
