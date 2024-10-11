# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/readers.py
"""Creates a `FixedLengthRecordDataset`.

    Args:
      filenames: A `tf.string` tensor containing one or more filenames.
      record_bytes: A `tf.int64` scalar representing the number of bytes in each
        record.
      header_bytes: (Optional.) A `tf.int64` scalar representing the number of
        bytes to skip at the start of a file.
      footer_bytes: (Optional.) A `tf.int64` scalar representing the number of
        bytes to ignore at the end of a file.
      buffer_size: (Optional.) A `tf.int64` scalar representing the number of
        bytes to buffer when reading.
      compression_type: (Optional.) A `tf.string` scalar evaluating to one of
        `""` (no compression), `"ZLIB"`, or `"GZIP"`.
      name: (Optional.) A name for the tf.data operation.
    """
self._filenames = filenames
self._record_bytes = ops.convert_to_tensor(
    record_bytes, dtype=dtypes.int64, name="record_bytes")
self._header_bytes = convert.optional_param_to_tensor(
    "header_bytes", header_bytes)
self._footer_bytes = convert.optional_param_to_tensor(
    "footer_bytes", footer_bytes)
self._buffer_size = convert.optional_param_to_tensor(
    "buffer_size", buffer_size, _DEFAULT_READER_BUFFER_SIZE_BYTES)
self._compression_type = convert.optional_param_to_tensor(
    "compression_type",
    compression_type,
    argument_default="",
    argument_dtype=dtypes.string)
self._name = name

variant_tensor = gen_dataset_ops.fixed_length_record_dataset_v2(
    self._filenames,
    self._header_bytes,
    self._record_bytes,
    self._footer_bytes,
    self._buffer_size,
    self._compression_type,
    metadata=self._metadata.SerializeToString())
super(_FixedLengthRecordDataset, self).__init__(variant_tensor)
