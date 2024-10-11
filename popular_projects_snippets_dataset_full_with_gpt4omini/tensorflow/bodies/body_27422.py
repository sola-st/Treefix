# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_batched_features_dataset_test.py
# Basic test: read from file 0.
outputs = self.make_batch_feature(
    filenames=self._filenames[0],
    label_key="label",
    num_epochs=num_epochs,
    batch_size=batch_size,
    drop_final_batch=True)
for tensor in nest.flatten(outputs):
    if isinstance(tensor, ops.Tensor):  # Guard against SparseTensor.
        self.assertEqual(tensor.shape[0], batch_size)
