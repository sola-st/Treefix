# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/tf_record_writer_test.py
self.evaluate(self.writer_fn(self._createFile()))
for i, r in enumerate(tf_record.tf_record_iterator(self._outputFilename())):
    self.assertAllEqual(self._record(i), r)
