# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2.py
for kwarg in kwargs:
    if kwarg not in [_PARTITION_SHAPE, _PARTITION_OFFSET]:
        raise TypeError(
            "Keyword argument should be one of "
            f"{list([_PARTITION_SHAPE, _PARTITION_OFFSET])}. Received: {kwarg}")
    elif not support_partition:
        raise ValueError(
            f"{self.__class__.__name__} initializer doesn't support "
            "partition-related arguments")
