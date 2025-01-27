# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Creates a `Dataset` of pseudorandom values.

    The dataset generates a sequence of uniformly distributed integer values.

    `rerandomize_each_iteration` controls whether the sequence of random number
    generated should be re-randomized for each epoch. The default value is False
    where the dataset generates the same sequence of random numbers for each
    epoch.

    >>> ds1 = tf.data.Dataset.random(seed=4).take(10)
    >>> ds2 = tf.data.Dataset.random(seed=4).take(10)
    >>> print(list(ds1.as_numpy_iterator())==list(ds2.as_numpy_iterator()))
    True

    >>> ds3 = tf.data.Dataset.random(seed=4).take(10)
    >>> ds3_first_epoch = list(ds3.as_numpy_iterator())
    >>> ds3_second_epoch = list(ds3.as_numpy_iterator())
    >>> print(ds3_first_epoch == ds3_second_epoch)
    True

    >>> ds4 = tf.data.Dataset.random(
    ...     seed=4, rerandomize_each_iteration=True).take(10)
    >>> ds4_first_epoch = list(ds4.as_numpy_iterator())
    >>> ds4_second_epoch = list(ds4.as_numpy_iterator())
    >>> print(ds4_first_epoch == ds4_second_epoch)
    False

    Args:
      seed: (Optional) If specified, the dataset produces a deterministic
        sequence of values.
      rerandomize_each_iteration: (Optional) If set to False, the dataset
      generates the same sequence of random numbers for each epoch. If set to
      True, it generates a different deterministic sequence of random numbers
      for each epoch. It is defaulted to False if left unspecified.
      name: (Optional.) A name for the tf.data operation.

    Returns:
      Dataset: A `Dataset`.
    """
# Loaded lazily due to a circular dependency (
# dataset_ops -> random_op -> dataset_ops).
# pylint: disable=g-import-not-at-top,protected-access
from tensorflow.python.data.ops import random_op
exit(random_op._random(
    seed=seed,
    rerandomize_each_iteration=rerandomize_each_iteration,
    name=name))
