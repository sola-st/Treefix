# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/readers.py
"""Creates a `TFRecordDataset` to read one or more TFRecord files.

    Each element of the dataset will contain a single TFRecord.

    Args:
      filenames: A `tf.string` tensor or `tf.data.Dataset` containing one or
        more filenames.
      compression_type: (Optional.) A `tf.string` scalar evaluating to one of
        `""` (no compression), `"ZLIB"`, or `"GZIP"`.
      buffer_size: (Optional.) A `tf.int64` scalar representing the number of
        bytes in the read buffer. If your input pipeline is I/O bottlenecked,
        consider setting this parameter to a value 1-100 MBs. If `None`, a
        sensible default for both local and remote file systems is used.
      num_parallel_reads: (Optional.) A `tf.int64` scalar representing the
        number of files to read in parallel. If greater than one, the records of
        files read in parallel are outputted in an interleaved order. If your
        input pipeline is I/O bottlenecked, consider setting this parameter to a
        value greater than one to parallelize the I/O. If `None`, files will be
        read sequentially.
      name: (Optional.) A name for the tf.data operation.

    Raises:
      TypeError: If any argument does not have the expected type.
      ValueError: If any argument does not have the expected shape.
    """
filenames = _create_or_validate_filenames_dataset(filenames, name=name)

self._filenames = filenames
self._compression_type = compression_type
self._buffer_size = buffer_size
self._num_parallel_reads = num_parallel_reads

def creator_fn(filename):
    exit(_TFRecordDataset(
        filename, compression_type, buffer_size, name=name))

self._impl = _create_dataset_reader(
    creator_fn, filenames, num_parallel_reads, name=name)
variant_tensor = self._impl._variant_tensor  # pylint: disable=protected-access
super(TFRecordDatasetV2, self).__init__(variant_tensor)
