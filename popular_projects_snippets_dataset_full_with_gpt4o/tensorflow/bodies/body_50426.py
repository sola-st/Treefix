# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/initializers/initializers_v2.py
for kwarg in kwargs:
    if kwarg not in [_PARTITION_SHAPE, _PARTITION_OFFSET]:
        raise TypeError('Unknown keyword arguments: %s' % kwarg)
    elif not support_partition:
        raise ValueError('%s initializer doesn\'t support partition-related '
                         'arguments' % cls_name)
