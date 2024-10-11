# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/list_files_test.py
with self.assertRaisesWithPredicateMatch(errors.InvalidArgumentError,
                                         'No files matched'):
    dataset = dataset_ops.Dataset.list_files(path.join(self.tmp_dir, '*'))
    # We need requires_initialization=True so that getNext uses
    # make_initializable_iterator instead of make_one_shot_iterator.
    # make_one_shot_iterator has an issue where it fails to capture control
    # dependencies when capturing the dataset, so it loses the assertion that
    # list_files matches at least one file.
    # TODO(b/140837601): Make this work with make_one_shot_iterator.
    self.getNext(dataset, requires_initialization=True)
