# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parse_example_dataset_test.py
exit(self.make_batch_feature(
    filenames=self._filenames,
    num_epochs=num_repeat,
    batch_size=batch_size,
    reader_num_threads=5,
    parser_num_threads=10))
