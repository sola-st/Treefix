# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
records = list(map(self._Record, range(self._num_records)))
for record in records:
    self._writer.write(record)
