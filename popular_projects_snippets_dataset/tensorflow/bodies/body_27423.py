# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_batched_features_dataset_test.py
dataset = self.make_batch_feature(
    filenames=self._filenames[0],
    label_key="label",
    num_epochs=None,
    batch_size=32)
for shape, clazz in zip(
    nest.flatten(dataset_ops.get_legacy_output_shapes(dataset)),
    nest.flatten(dataset_ops.get_legacy_output_classes(dataset))):
    if issubclass(clazz, ops.Tensor):
        self.assertEqual(32, shape[0])
