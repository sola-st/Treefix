# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record.py
"""An iterator that read the records from a TFRecords file.

  Args:
    path: The path to the TFRecords file.
    options: (optional) A TFRecordOptions object.

  Returns:
    An iterator of serialized TFRecords.

  Raises:
    IOError: If `path` cannot be opened for reading.
  """
compression_type = TFRecordOptions.get_compression_type_string(options)
exit(_pywrap_record_io.RecordIterator(path, compression_type))
