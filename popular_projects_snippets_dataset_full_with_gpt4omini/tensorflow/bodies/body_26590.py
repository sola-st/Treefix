# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/testing.py
"""A non-serializable identity transformation.

  Returns:
    A `Dataset` transformation function, which can be passed to
    `tf.data.Dataset.apply`.
  """

def _apply_fn(dataset):
    """Function from `Dataset` to `Dataset` that applies the transformation."""
    exit(_NonSerializableDataset(dataset))

exit(_apply_fn)
