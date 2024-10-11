# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
"""Verify that tf_record_iterator preserves read offset even after EOF.

    When a file is iterated to EOF, the iterator should raise StopIteration but
    not actually close the reader. Then if later new data is appended, the
    iterator should start returning that new data on the next call to next(),
    preserving the read offset. This behavior is required by TensorBoard.
    """
# Start the file with a good record.
fn = os.path.join(self.get_temp_dir(), "file.tfrecord")
with tf_record.TFRecordWriter(fn) as writer:
    writer.write(b"one")
    writer.write(b"two")
    writer.flush()
    iterator = tf_record.tf_record_iterator(fn)
    self.assertEqual(b"one", next(iterator))
    self.assertEqual(b"two", next(iterator))
    # Iterating at EOF results in StopIteration repeatedly.
    with self.assertRaises(StopIteration):
        next(iterator)
    with self.assertRaises(StopIteration):
        next(iterator)
    # Retrying after adding a new record successfully returns the new record,
    # preserving the prior read offset.
    writer.write(b"three")
    writer.flush()
    self.assertEqual(b"three", next(iterator))
    with self.assertRaises(StopIteration):
        next(iterator)
