# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_batched_features_dataset_test.py
# Basic test: read from file 0.
self.outputs = self.getNext(
    self.make_batch_feature(
        filenames=self._filenames[0],
        label_key="label",
        num_epochs=num_epochs,
        batch_size=batch_size))
self._verify_records(
    batch_size, 0, num_epochs=num_epochs, label_key_provided=True)
with self.assertRaises(errors.OutOfRangeError):
    self._next_actual_batch(label_key_provided=True)

    # Basic test: read from file 1.
self.outputs = self.getNext(
    self.make_batch_feature(
        filenames=self._filenames[1],
        label_key="label",
        num_epochs=num_epochs,
        batch_size=batch_size))
self._verify_records(
    batch_size, 1, num_epochs=num_epochs, label_key_provided=True)
with self.assertRaises(errors.OutOfRangeError):
    self._next_actual_batch(label_key_provided=True)

# Basic test: read from both files.
self.outputs = self.getNext(
    self.make_batch_feature(
        filenames=self._filenames,
        label_key="label",
        num_epochs=num_epochs,
        batch_size=batch_size))
self._verify_records(
    batch_size, num_epochs=num_epochs, label_key_provided=True)
with self.assertRaises(errors.OutOfRangeError):
    self._next_actual_batch(label_key_provided=True)
# Basic test: read from both files.
self.outputs = self.getNext(
    self.make_batch_feature(
        filenames=self._filenames,
        num_epochs=num_epochs,
        batch_size=batch_size))
self._verify_records(batch_size, num_epochs=num_epochs)
with self.assertRaises(errors.OutOfRangeError):
    self._next_actual_batch()
