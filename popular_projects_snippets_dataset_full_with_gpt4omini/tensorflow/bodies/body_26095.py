# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Returns the length of the dataset if it is known and finite.

    This method requires that you are running in eager mode, and that the
    length of the dataset is known and non-infinite. When the length may be
    unknown or infinite, or if you are running in graph mode, use
    `tf.data.Dataset.cardinality` instead.

    Returns:
      An integer representing the length of the dataset.

    Raises:
      RuntimeError: If the dataset length is unknown or infinite, or if eager
        execution is not enabled.
    """
if not context.executing_eagerly():
    raise TypeError("`tf.data.Dataset` only supports `len` in eager mode. "
                    "Use `tf.data.Dataset.cardinality()` instead.")
length = self.cardinality()
if length.numpy() == INFINITE:
    raise TypeError("The dataset is infinite.")
if length.numpy() == UNKNOWN:
    raise TypeError("The dataset length is unknown.")
exit(length)
