# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2.py
"""Returns a tensor object initialized as specified by the initializer.

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. If not provided will return tensor
        of `tf.float32`.
      **kwargs: Additional keyword arguments. Accepted values:
        `partition_shape` and `partition_offset`. Used when creating a single
        partition in a partitioned variable. `partition_shape` is the shape of
        the partition (i.e. the shape of the returned tensor) and
        `partition_offset` is a tuple of `int` specifying the offset of this
        partition w.r.t each axis. For example, a tensor of shape `(30, 100)`
        can be partitioned into two partitions: `p0` of shape `(10, 100)` and
        `p1` of shape `(20, 100)`; if the initializer is called with
        `partition_shape=(20, 100)` and `partition_offset=(10, 0)`, it should
        return the value for `p1`.
    """
raise NotImplementedError
