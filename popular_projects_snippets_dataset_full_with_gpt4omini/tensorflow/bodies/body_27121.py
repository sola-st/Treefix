# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_tf_record_dataset_test.py
dataset = readers.make_tf_record_dataset(
    file_pattern=self._filenames, num_epochs=None, batch_size=32)
for shape in nest.flatten(dataset_ops.get_legacy_output_shapes(dataset)):
    self.assertEqual(32, shape[0])
