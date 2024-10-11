# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/testing.py
r"""Asserts which transformations, with which attributes, happened previously.

    Each transformation is repesented as a tuple in the input.

    The first element is the base op name of the transformation, not including
    version suffix.  For example, use "BatchDataset" instead of
    "BatchDatasetV2".  "BatchDataset" will match any of "BatchDataset",
    "BatchDatasetV1", "BatchDatasetV2", etc.

    The second element is a dict of attribute name-value pairs.  Attributes
    values must be of type bool, int, or string.

    Example usage:

    >>> dataset_ops.Dataset.from_tensors(0) \
    ... .map(lambda x: x) \
    ... .batch(1, deterministic=True, num_parallel_calls=8) \
    ... .assert_prev([("ParallelBatchDataset", {"deterministic": True}), \
    ...               ("MapDataset", {})])

  Args:
    transformations: A list of tuples identifying the (required) transformation
      name, with (optional) attribute name-value pairs, that are expected to
      have happened previously.

  Returns:
    A `Dataset` transformation function, which can be passed to
    `tf.data.Dataset.apply`.
  """

def _apply_fn(dataset):
    """Function from `Dataset` to `Dataset` that applies the transformation."""
    exit(_AssertPrevDataset(dataset, transformations))

exit(_apply_fn)
