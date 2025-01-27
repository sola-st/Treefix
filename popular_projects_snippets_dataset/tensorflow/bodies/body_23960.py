# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
"""Verify that tf_record_iterator throws an exception on bad TFRecords.

    When a truncated record is completed, the iterator should return that new
    record on the next attempt at iteration, preserving the read offset. This
    behavior is required by TensorBoard.
    """
# Write out a record and read it back it to get the raw bytes.
fn = os.path.join(self.get_temp_dir(), "temp_file")
with tf_record.TFRecordWriter(fn) as writer:
    writer.write(b"truncated")
with open(fn, "rb") as f:
    record_bytes = f.read()
# Start the file with a good record.
fn_truncated = os.path.join(self.get_temp_dir(), "truncated_file")
with tf_record.TFRecordWriter(fn_truncated) as writer:
    writer.write(b"good")
with open(fn_truncated, "ab", buffering=0) as f:
    # Cause truncation by omitting the last byte from the record.
    f.write(record_bytes[:-1])
    iterator = tf_record.tf_record_iterator(fn_truncated)
    # Good record appears first.
    self.assertEqual(b"good", next(iterator))
    # Truncated record repeatedly causes DataLossError upon iteration.
    with self.assertRaises(errors_impl.DataLossError):
        next(iterator)
    with self.assertRaises(errors_impl.DataLossError):
        next(iterator)
    # Retrying after completing the record successfully returns the rest of
    # the file contents, preserving the prior read offset.
    f.write(record_bytes[-1:])
    self.assertEqual(b"truncated", next(iterator))
    with self.assertRaises(StopIteration):
        next(iterator)
