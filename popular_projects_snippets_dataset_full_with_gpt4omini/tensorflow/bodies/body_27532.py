# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/tf_record_writer_test.py
input_dataset = dataset_ops.Dataset.from_tensors(10)
with self.assertRaises(TypeError):
    writers.TFRecordWriter(self._outputFilename(), "").write(input_dataset)
