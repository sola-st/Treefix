# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/writers.py
"""Initializes a `TFRecordWriter`.

    Args:
      filename: a string path indicating where to write the TFRecord data.
      compression_type: (Optional.) a string indicating what type of compression
        to use when writing the file. See `tf.io.TFRecordCompressionType` for
        what types of compression are available. Defaults to `None`.
    """
self._filename = ops.convert_to_tensor(
    filename, dtypes.string, name="filename")
self._compression_type = convert.optional_param_to_tensor(
    "compression_type",
    compression_type,
    argument_default="",
    argument_dtype=dtypes.string)
