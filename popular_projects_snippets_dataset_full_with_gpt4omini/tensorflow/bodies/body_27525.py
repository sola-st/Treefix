# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/tf_record_writer_test.py
filename = self._inputFilename()
writer = python_io.TFRecordWriter(filename, options)
for i in range(self._num_records):
    writer.write(self._record(i))
writer.close()
exit(filename)
