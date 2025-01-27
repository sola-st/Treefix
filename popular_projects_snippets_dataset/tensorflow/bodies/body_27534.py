# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/tf_record_writer_test.py
input_dataset = readers.TFRecordDataset(self._createFile())
exit(writers.TFRecordWriter(self._outputFilename()).write(input_dataset))
