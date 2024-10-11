# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record.py
"""Opens file `path` and creates a `TFRecordWriter` writing to it.

    Args:
      path: The path to the TFRecords file.
      options: (optional) String specifying compression type,
          `TFRecordCompressionType`, or `TFRecordOptions` object.

    Raises:
      IOError: If `path` cannot be opened for writing.
      ValueError: If valid compression_type can't be determined from `options`.
    """
if not isinstance(options, TFRecordOptions):
    options = TFRecordOptions(compression_type=options)

# pylint: disable=protected-access
super(TFRecordWriter, self).__init__(
    compat.as_bytes(path), options._as_record_writer_options())
