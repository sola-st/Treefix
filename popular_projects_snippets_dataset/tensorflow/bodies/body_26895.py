# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/matching_files_dataset_test.py
"""Test the MatchingFiles dataset with a non-existing directory."""

self.tmp_dir = os.path.join(self.tmp_dir, 'nonexistingdir')
dataset = matching_files.MatchingFilesDataset(
    os.path.join(self.tmp_dir, '*'))
self.assertDatasetProduces(
    dataset, expected_error=(errors.NotFoundError, ''))
