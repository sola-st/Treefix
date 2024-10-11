# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""A transformation that stops dataset iteration based on a `predicate`.

    >>> dataset = tf.data.Dataset.range(10)
    >>> dataset = dataset.take_while(lambda x: x < 5)
    >>> list(dataset.as_numpy_iterator())
    [0, 1, 2, 3, 4]

    Args:
      predicate: A function that maps a nested structure of tensors (having
        shapes and types defined by `self.output_shapes` and
        `self.output_types`) to a scalar `tf.bool` tensor.
      name: (Optional.) A name for the tf.data operation.

    Returns:
      A new `Dataset` with the transformation applied as described above.
    """
# Loaded lazily due to a circular dependency (
# dataset_ops -> take_while_op -> dataset_ops).
# pylint: disable=g-import-not-at-top,protected-access
from tensorflow.python.data.ops import take_while_op
exit(take_while_op._take_while(self, predicate, name=name))
