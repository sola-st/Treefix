# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Constructs a RecordInput Op.

    Args:
      file_pattern: File path to the dataset, possibly containing wildcards.
        All matching files will be iterated over each epoch.
      batch_size: How many records to return at a time.
      buffer_size: The maximum number of records the buffer will contain.
      parallelism: How many reader threads to use for reading from files.
      shift_ratio: What percentage of the total number files to move the start
        file forward by each epoch.
      seed: Specify the random number seed used by generator that randomizes
        records.
      name: Optional name for the operation.
      batches: None by default, creating a single batch op. Otherwise specifies
        how many batches to create, which are returned as a list when
        `get_yield_op()` is called. An example use case is to split processing
        between devices on one computer.
      compression_type: The type of compression for the file. Currently ZLIB and
        GZIP are supported. Defaults to none.

    Raises:
      ValueError: If one of the arguments is invalid.
    """
self._batch_size = batch_size
if batches is not None:
    self._batch_size *= batches
self._batches = batches
self._file_pattern = file_pattern
self._buffer_size = buffer_size
self._parallelism = parallelism
self._shift_ratio = shift_ratio
self._seed = seed
self._name = name
self._compression_type = python_io.TFRecordCompressionType.NONE
if compression_type is not None:
    self._compression_type = compression_type
