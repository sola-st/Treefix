# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/tf_record_writer_test.py
with self.assertRaises(TypeError):
    writers.TFRecordWriter(self._outputFilename(), "").write("whoops")
