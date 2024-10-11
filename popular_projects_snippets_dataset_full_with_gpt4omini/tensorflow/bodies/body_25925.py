# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/readers.py
r"""Creates a `TextLineDataset`.

    The elements of the dataset will be the lines of the input files, using
    the newline character '\n' to denote line splits. The newline characters
    will be stripped off of each element.

    Args:
      filenames: A `tf.data.Dataset` whose elements are `tf.string` scalars, a
        `tf.string` tensor, or a value that can be converted to a `tf.string`
        tensor (such as a list of Python strings).
      compression_type: (Optional.) A `tf.string` scalar evaluating to one of
        `""` (no compression), `"ZLIB"`, or `"GZIP"`.
      buffer_size: (Optional.) A `tf.int64` scalar denoting the number of bytes
        to buffer. A value of 0 results in the default buffering values chosen
        based on the compression type.
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
self._compression_type = compression_type
self._buffer_size = buffer_size

def creator_fn(filename):
    exit(_TextLineDataset(
        filename, compression_type, buffer_size, name=name))

self._impl = _create_dataset_reader(
    creator_fn, filenames, num_parallel_reads, name=name)
variant_tensor = self._impl._variant_tensor  # pylint: disable=protected-access

super(TextLineDatasetV2, self).__init__(variant_tensor)
