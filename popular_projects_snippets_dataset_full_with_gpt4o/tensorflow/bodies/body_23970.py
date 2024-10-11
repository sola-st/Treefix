# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
records = list(map(self._Record, range(self._num_records)))
for record in records:
    self._writer.write(record)
self._writer.flush()

actual = list(tf_record.tf_record_iterator(self._fn, self._options))
self.assertListEqual(actual, records)
