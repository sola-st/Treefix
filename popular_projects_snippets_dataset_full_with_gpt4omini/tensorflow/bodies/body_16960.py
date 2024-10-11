# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/io_ops.py
"""Creates a new ReaderBase.

    Args:
      reader_ref: The operation that implements the reader.
      supports_serialize: True if the reader implementation can
        serialize its state.

    Raises:
      RuntimeError: If eager execution is enabled.
    """
if context.executing_eagerly():
    raise RuntimeError(
        "Readers are not supported when eager execution is enabled. "
        "Instead, please use tf.data to get data into your model.")

self._reader_ref = reader_ref
self._supports_serialize = supports_serialize
