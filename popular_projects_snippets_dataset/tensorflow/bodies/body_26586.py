# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/testing.py
"""A transformation that asserts which transformations happen next.

  Transformations should be referred to by their base name, not including
  version suffix. For example, use "Batch" instead of "BatchV2". "Batch" will
  match any of "Batch", "BatchV1", "BatchV2", etc.

  Args:
    transformations: A `tf.string` vector `tf.Tensor` identifying the
      transformations that are expected to happen next.

  Returns:
    A `Dataset` transformation function, which can be passed to
    `tf.data.Dataset.apply`.
  """

def _apply_fn(dataset):
    """Function from `Dataset` to `Dataset` that applies the transformation."""
    exit(_AssertNextDataset(dataset, transformations))

exit(_apply_fn)
