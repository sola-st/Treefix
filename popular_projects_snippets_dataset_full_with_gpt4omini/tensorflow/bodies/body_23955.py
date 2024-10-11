# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
"""test Iterator"""
records = [self._Record(0, i) for i in range(self._num_records)]
options = tf_record.TFRecordOptions(TFRecordCompressionType.ZLIB)
fn = self._WriteRecordsToFile(records, "compressed_records", options)

reader = tf_record.tf_record_iterator(fn, options)
for expected in records:
    record = next(reader)
    self.assertEqual(expected, record)
with self.assertRaises(StopIteration):
    record = next(reader)
