# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
"""Test read access to random offsets in the TFRecord file."""
records = [self._Record(0, i) for i in range(self._num_records)]
fn = self._WriteRecordsToFile(records, "uncompressed_records")
reader = tf_record.tf_record_random_reader(fn)

offset = 0
offsets = [offset]
# Do a pass of forward reading.
for i in range(self._num_records):
    record, offset = reader.read(offset)
    self.assertEqual(record, records[i])
    offsets.append(offset)
# Reading off the bound should lead to error.
with self.assertRaisesRegex(IndexError, r"Out of range.*offset"):
    reader.read(offset)
# Do a pass of backward reading.
for i in range(self._num_records - 1, 0, -1):
    record, offset = reader.read(offsets[i])
    self.assertEqual(offset, offsets[i + 1])
    self.assertEqual(record, records[i])
