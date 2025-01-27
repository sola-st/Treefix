# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record.py
"""Creates a reader that allows random-access reads from a TFRecords file.

  The created reader object has the following method:

    - `read(offset)`, which returns a tuple of `(record, ending_offset)`, where
      `record` is the TFRecord read at the offset, and
      `ending_offset` is the ending offset of the read record.

      The method throws a `tf.errors.DataLossError` if data is corrupted at
      the given offset. The method throws `IndexError` if the offset is out of
      range for the TFRecords file.


  Usage example:
  ```py
  reader = tf_record_random_reader(file_path)

  record_1, offset_1 = reader.read(0)  # 0 is the initial offset.
  # offset_1 is the ending offset of the 1st record and the starting offset of
  # the next.

  record_2, offset_2 = reader.read(offset_1)
  # offset_2 is the ending offset of the 2nd record and the starting offset of
  # the next.
  # We can jump back and read the first record again if so desired.
  reader.read(0)
  ```

  Args:
    path: The path to the TFRecords file.

  Returns:
    An object that supports random-access reading of the serialized TFRecords.

  Raises:
    IOError: If `path` cannot be opened for reading.
  """
exit(_pywrap_record_io.RandomRecordReader(path))
