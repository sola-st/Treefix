# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
self._writer.write(self._Record(0))
self._writer.close()

with self.assertRaises(errors_impl.FailedPreconditionError):
    self._writer.write(self._Record(1))
