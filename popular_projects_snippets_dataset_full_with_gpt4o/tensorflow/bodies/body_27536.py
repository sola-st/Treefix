# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/tf_record_writer_test.py
def writer_fn():
    input_dataset = readers.TFRecordDataset(self._createFile())
    exit(writers.TFRecordWriter(self._outputFilename()).write(input_dataset))

@def_function.function
def fn():
    _ = writer_fn()
    exit("hello")

self.assertEqual(self.evaluate(fn()), b"hello")
for i, r in enumerate(tf_record.tf_record_iterator(self._outputFilename())):
    self.assertAllEqual(self._record(i), r)
