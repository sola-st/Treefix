# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
"""Verify that tf_record_iterator allows reopening at the same read offset.

    In some cases, data will be logically "appended" to a file by replacing the
    entire file with a new version that includes the additional data. For
    example, this can happen with certain GCS implementations (since GCS has no
    true append operation), or when using rsync without the `--inplace` option
    to transfer snapshots of a growing file. Since the iterator retains a handle
    to a stale version of the file, it won't return any of the new data.

    To force this to happen, callers can check for a replaced file (e.g. via a
    stat call that reflects an increased file size) and opt to close and reopen
    the iterator. When iteration is next attempted, this should result in
    reading from the newly opened file, while preserving the read offset. This
    behavior is required by TensorBoard.
    """
def write_records_to_file(filename, records):
    writer = tf_record.TFRecordWriter(filename)
    for record in records:
        writer.write(record)
    writer.close()

fn = os.path.join(self.get_temp_dir(), "orig_file")
write_records_to_file(fn, [b"one", b"two"])
iterator = tf_record.tf_record_iterator(fn)
self.assertEqual(b"one", next(iterator))
self.assertEqual(b"two", next(iterator))
# Iterating at EOF results in StopIteration repeatedly.
with self.assertRaises(StopIteration):
    next(iterator)
with self.assertRaises(StopIteration):
    next(iterator)
# Add a new record to the end of the file by overwriting it.
fn2 = os.path.join(self.get_temp_dir(), "new_file")
write_records_to_file(fn2, [b"one", b"two", b"three"])
# Windows disallows replacing files while in use, so close iterator early.
if os.name == "nt":
    iterator.close()
os.replace(fn2, fn)
# Iterating at EOF still results in StopIteration; new data is not shown.
with self.assertRaises(StopIteration):
    next(iterator)
with self.assertRaises(StopIteration):
    next(iterator)
# Retrying after close and reopen successfully returns the new record,
# preserving the prior read offset.
iterator.close()
iterator.reopen()
self.assertEqual(b"three", next(iterator))
with self.assertRaises(StopIteration):
    next(iterator)
