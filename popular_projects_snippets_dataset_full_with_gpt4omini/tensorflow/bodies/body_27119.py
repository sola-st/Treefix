# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_tf_record_dataset_test.py
exit(readers.make_tf_record_dataset(
    file_pattern=self._filenames,
    num_epochs=num_epochs,
    batch_size=batch_size,
    num_parallel_reads=num_parallel_reads,
    shuffle=True,
    shuffle_seed=seed))
