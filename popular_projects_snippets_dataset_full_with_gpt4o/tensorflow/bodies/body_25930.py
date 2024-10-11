# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/readers.py
"""Creates a `TFRecordDataset`.

    Args:
      filenames: A `tf.string` tensor containing one or more filenames.
      compression_type: (Optional.) A `tf.string` scalar evaluating to one of
        `""` (no compression), `"ZLIB"`, or `"GZIP"`.
      buffer_size: (Optional.) A `tf.int64` scalar representing the number of
        bytes in the read buffer. 0 means no buffering.
      name: (Optional.) A name for the tf.data operation.
    """
self._filenames = filenames
self._compression_type = convert.optional_param_to_tensor(
    "compression_type",
    compression_type,
    argument_default="",
    argument_dtype=dtypes.string)
self._buffer_size = convert.optional_param_to_tensor(
    "buffer_size",
    buffer_size,
    argument_default=_DEFAULT_READER_BUFFER_SIZE_BYTES)
self._name = name

variant_tensor = gen_dataset_ops.tf_record_dataset(
    self._filenames, self._compression_type, self._buffer_size,
    metadata=self._metadata.SerializeToString())
super(_TFRecordDataset, self).__init__(variant_tensor)
