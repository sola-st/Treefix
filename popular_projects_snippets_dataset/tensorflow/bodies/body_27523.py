# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/tf_record_writer_test.py
input_dataset = readers.TFRecordDataset([filename], compression_type)
exit(writers.TFRecordWriter(self._outputFilename(),
                              compression_type).write(input_dataset))
