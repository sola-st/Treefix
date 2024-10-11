# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_test_base.py
if file_index is not None:
    if isinstance(file_index, list):
        file_indices = file_index
    else:
        file_indices = [file_index]
else:
    file_indices = range(self._num_files)

for expected_batch in self._next_expected_batch(
    file_indices, batch_size, num_epochs, interleave_cycle_length,
    drop_final_batch, use_parser_fn):
    actual_batch = self.evaluate(outputs())
    self.assertAllEqual(expected_batch, actual_batch)
