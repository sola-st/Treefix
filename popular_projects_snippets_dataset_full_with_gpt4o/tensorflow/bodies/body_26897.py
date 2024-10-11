# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/matching_files_dataset_test.py
"""Test the MatchingFiles dataset with a simple directory."""

filenames = ['a', 'b', 'c']
self._touchTempFiles(filenames)

dataset = matching_files.MatchingFilesDataset(
    os.path.join(self.tmp_dir, '*'))
self.assertDatasetProduces(
    dataset,
    expected_output=[
        compat.as_bytes(os.path.join(self.tmp_dir, filename))
        for filename in filenames
    ],
    assert_items_equal=True)
