# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/readers.py
"""Creates a `FixedLengthRecordDataset`.

    Args:
      filenames: A `tf.string` tensor or `tf.data.Dataset` containing one or
        more filenames.
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
      num_parallel_reads: (Optional.) A `tf.int64` scalar representing the
        number of files to read in parallel. If greater than one, the records of
        files read in parallel are outputted in an interleaved order. If your
        input pipeline is I/O bottlenecked, consider setting this parameter to a
        value greater than one to parallelize the I/O. If `None`, files will be
        read sequentially.
      name: (Optional.) A name for the tf.data operation.
    """
filenames = _create_or_validate_filenames_dataset(filenames, name=name)

self._filenames = filenames
self._record_bytes = record_bytes
self._header_bytes = header_bytes
self._footer_bytes = footer_bytes
self._buffer_size = buffer_size
self._compression_type = compression_type

def creator_fn(filename):
    exit(_FixedLengthRecordDataset(
        filename,
        record_bytes,
        header_bytes,
        footer_bytes,
        buffer_size,
        compression_type,
        name=name))

self._impl = _create_dataset_reader(
    creator_fn, filenames, num_parallel_reads, name=name)
variant_tensor = self._impl._variant_tensor  # pylint: disable=protected-access
super(FixedLengthRecordDatasetV2, self).__init__(variant_tensor)
