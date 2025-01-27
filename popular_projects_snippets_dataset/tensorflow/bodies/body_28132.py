# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_test_base.py
if file_index is not None:
    file_indices = [file_index]
else:
    file_indices = range(self._num_files)

for expected_batch in self._next_expected_batch(
    file_indices,
    batch_size,
    num_epochs,
    cycle_length=interleave_cycle_length):
    actual_batch = self._next_actual_batch(
        label_key_provided=label_key_provided)
    for i in range(len(expected_batch)):
        self.assertAllEqual(expected_batch[i], actual_batch[i])
