# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/tf_record_writer_test.py
options = tf_record.TFRecordOptions(tf_record.TFRecordCompressionType.GZIP)
self.evaluate(
    self.writer_fn(self._createFile(options), compression_type="GZIP"))
for i, r in enumerate(
    tf_record.tf_record_iterator(self._outputFilename(), options=options)):
    self.assertAllEqual(self._record(i), r)
