# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
records = [self._Record(0, i) for i in range(self._num_records)]
fn = self._WriteRecordsToFile(records, "uncompressed_records")
reader = tf_record.tf_record_random_reader(fn)
with self.assertRaisesRegex(errors_impl.DataLossError, r"corrupted record"):
    reader.read(1)  # 1 is guaranteed to be an invalid offset.
