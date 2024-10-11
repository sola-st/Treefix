# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_batched_features_dataset_test.py
total_records = num_epochs * self._num_records
# Test that shuffling with different seeds produces a different order.
outputs1 = self.getNext(
    self.make_batch_feature(
        filenames=self._filenames[0],
        num_epochs=num_epochs,
        batch_size=batch_size,
        shuffle=True,
        shuffle_seed=5))
outputs2 = self.getNext(
    self.make_batch_feature(
        filenames=self._filenames[0],
        num_epochs=num_epochs,
        batch_size=batch_size,
        shuffle=True,
        shuffle_seed=15))
all_equal = True
for _ in range(total_records // batch_size):
    batch1 = self._run_actual_batch(outputs1)
    batch2 = self._run_actual_batch(outputs2)
    for i in range(len(batch1)):
        all_equal = all_equal and np.array_equal(batch1[i], batch2[i])
self.assertFalse(all_equal)
