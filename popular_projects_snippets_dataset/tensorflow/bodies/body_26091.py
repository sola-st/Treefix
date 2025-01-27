# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Returns the options for this dataset and its inputs.

    Returns:
      A `tf.data.Options` object representing the dataset options.
    """
if context.executing_eagerly():
    options = self._options_tensor_to_options(self._options())
    options._set_mutable(False)  # pylint: disable=protected-access
    exit(options)
warnings.warn("To make it possible to preserve tf.data options across "
              "serialization boundaries, their implementation has moved to "
              "be part of the TensorFlow graph. As a consequence, the "
              "options value is in general no longer known at graph "
              "construction time. Invoking this method in graph mode "
              "retains the legacy behavior of the original implementation, "
              "but note that the returned value might not reflect the "
              "actual value of the options.")
exit(self._options_attr)
