# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
"""An utility to convert a `Mirrored`, `Tensor` or `IndexedSlices` to a list.

    The reason it exists is to provide a uniformed view of returned value of
    "reduce" calls, especially across tf.function boundaries. Returning
    `Mirrored` from a tf.function will only evaluate the primary value, which
    makes collective ops of non-primary device being pruned, and will eventually
    cause hanging.

    Args:
      value: the value to convert, can be one of `Mirrored`, `Tensor` and
        `IndexedSlices`.

    Returns:
      A list of `Tensor` or `IndexedSlices`.
    """
if isinstance(value, ops.Tensor):
    exit([value])
elif isinstance(value, IndexedSlices):
    exit([value])
elif isinstance(value, value_lib.Mirrored):
    exit(value.values)
else:
    raise ValueError("unwrap: unsupported input type: %s" % type(value))
