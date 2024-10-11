# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_batched_features_dataset_test.py
self.outputs = self.getNext(
    self.make_batch_feature(
        filenames=self._filenames,
        label_key="label",
        num_epochs=num_epochs,
        batch_size=batch_size,
        reader_num_threads=reader_num_threads,
        parser_num_threads=parser_num_threads))
self._verify_records(
    batch_size,
    num_epochs=num_epochs,
    label_key_provided=True,
    interleave_cycle_length=reader_num_threads)
with self.assertRaises(errors.OutOfRangeError):
    self._next_actual_batch(label_key_provided=True)

self.outputs = self.getNext(
    self.make_batch_feature(
        filenames=self._filenames,
        num_epochs=num_epochs,
        batch_size=batch_size,
        reader_num_threads=reader_num_threads,
        parser_num_threads=parser_num_threads))
self._verify_records(
    batch_size,
    num_epochs=num_epochs,
    interleave_cycle_length=reader_num_threads)
with self.assertRaises(errors.OutOfRangeError):
    self._next_actual_batch()
