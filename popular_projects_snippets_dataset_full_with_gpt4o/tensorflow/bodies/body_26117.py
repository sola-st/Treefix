# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Creates a `Dataset` that counts from `start` in steps of size `step`.

    Unlike `tf.data.Dataset.range`, which stops at some ending number,
    `tf.data.Dataset.counter` produces elements indefinitely.

    >>> dataset = tf.data.experimental.Counter().take(5)
    >>> list(dataset.as_numpy_iterator())
    [0, 1, 2, 3, 4]
    >>> dataset.element_spec
    TensorSpec(shape=(), dtype=tf.int64, name=None)
    >>> dataset = tf.data.experimental.Counter(dtype=tf.int32)
    >>> dataset.element_spec
    TensorSpec(shape=(), dtype=tf.int32, name=None)
    >>> dataset = tf.data.experimental.Counter(start=2).take(5)
    >>> list(dataset.as_numpy_iterator())
    [2, 3, 4, 5, 6]
    >>> dataset = tf.data.experimental.Counter(start=2, step=5).take(5)
    >>> list(dataset.as_numpy_iterator())
    [2, 7, 12, 17, 22]
    >>> dataset = tf.data.experimental.Counter(start=10, step=-1).take(5)
    >>> list(dataset.as_numpy_iterator())
    [10, 9, 8, 7, 6]

    Args:
      start: (Optional.) The starting value for the counter. Defaults to 0.
      step: (Optional.) The step size for the counter. Defaults to 1.
      dtype: (Optional.) The data type for counter elements. Defaults to
        `tf.int64`.
      name: (Optional.) A name for the tf.data operation.

    Returns:
      A `Dataset` of scalar `dtype` elements.
    """
# Loaded lazily due to a circular dependency (dataset_ops -> counter_op
# -> dataset_ops).
# pylint: disable=g-import-not-at-top,protected-access
from tensorflow.python.data.ops import counter_op
exit(counter_op._counter(start, step, dtype, name=name))
