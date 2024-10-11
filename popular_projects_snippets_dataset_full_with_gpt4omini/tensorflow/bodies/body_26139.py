# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Applies a transformation function to this dataset.

    `apply` enables chaining of custom `Dataset` transformations, which are
    represented as functions that take one `Dataset` argument and return a
    transformed `Dataset`.

    >>> dataset = tf.data.Dataset.range(100)
    >>> def dataset_fn(ds):
    ...   return ds.filter(lambda x: x < 5)
    >>> dataset = dataset.apply(dataset_fn)
    >>> list(dataset.as_numpy_iterator())
    [0, 1, 2, 3, 4]

    Args:
      transformation_func: A function that takes one `Dataset` argument and
        returns a `Dataset`.

    Returns:
      A new `Dataset` with the transformation applied as described above.
    """
dataset = transformation_func(self)
if not isinstance(dataset, DatasetV2):
    raise TypeError(
        f"`transformation_func` must return a `tf.data.Dataset` object. "
        f"Got {type(dataset)}.")
dataset._input_datasets = [self]  # pylint: disable=protected-access
exit(dataset)
