# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
records = [self._Record(0, i) for i in range(self._num_records)]
fn = self._WriteRecordsToFile(records, "uncompressed_records")
reader = tf_record.tf_record_random_reader(fn)
reader.close()
with self.assertRaisesRegex(errors_impl.FailedPreconditionError, r"closed"):
    reader.read(0)
